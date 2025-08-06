from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils import timezone
import json

from apps.inventory.models import MenuItem, Category
from .models import Cart, CartItem, CustomerOrder, CustomerOrderItem


def get_or_create_cart(request):
    """Get or create a cart for the current session"""
    if not request.session.session_key:
        request.session.create()
    
    cart, created = Cart.objects.get_or_create(session_key=request.session.session_key)
    return cart


def menu_view(request):
    """Display menu items organized by categories"""
    categories = Category.objects.prefetch_related('menu_items').all()
    search_query = request.GET.get('search', '')
    
    if search_query:
        menu_items = MenuItem.objects.filter(
            Q(name__icontains=search_query) | 
            Q(description__icontains=search_query),
            is_available=True
        ).select_related('category')
    else:
        menu_items = MenuItem.objects.filter(is_available=True).select_related('category')
    
    # Group items by category
    menu_by_category = {}
    for category in categories:
        category_items = menu_items.filter(category=category)
        if category_items.exists():
            menu_by_category[category] = category_items
    
    cart = get_or_create_cart(request)
    
    context = {
        'menu_by_category': menu_by_category,
        'search_query': search_query,
        'cart': cart,
    }
    return render(request, 'customer_interface/menu.html', context)


def add_to_cart(request):
    """Add item to cart via AJAX"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            menu_item_id = data.get('menu_item_id')
            quantity = int(data.get('quantity', 1))
            
            menu_item = get_object_or_404(MenuItem, id=menu_item_id, is_available=True)
            cart = get_or_create_cart(request)
            
            # Check if item already exists in cart
            cart_item, created = CartItem.objects.get_or_create(
                cart=cart,
                menu_item=menu_item,
                defaults={'quantity': quantity}
            )
            
            if not created:
                cart_item.quantity += quantity
                cart_item.save()
            
            return JsonResponse({
                'success': True,
                'message': f'{menu_item.name} added to cart',
                'cart_count': cart.item_count,
                'cart_total': float(cart.total_amount)
            })
            
        except (json.JSONDecodeError, ValueError, KeyError):
            return JsonResponse({'success': False, 'message': 'Invalid data'}, status=400)
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=500)
    
    return JsonResponse({'success': False, 'message': 'Invalid request method'}, status=405)


def update_cart_item(request, item_id):
    """Update cart item quantity"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            quantity = int(data.get('quantity', 1))
            
            cart_item = get_object_or_404(CartItem, id=item_id)
            
            if quantity <= 0:
                cart_item.delete()
                message = 'Item removed from cart'
            else:
                cart_item.quantity = quantity
                cart_item.save()
                message = 'Cart updated'
            
            cart = cart_item.cart
            return JsonResponse({
                'success': True,
                'message': message,
                'cart_count': cart.item_count,
                'cart_total': float(cart.total_amount),
                'item_subtotal': float(cart_item.subtotal) if quantity > 0 else 0
            })
            
        except (json.JSONDecodeError, ValueError):
            return JsonResponse({'success': False, 'message': 'Invalid data'}, status=400)
    
    return JsonResponse({'success': False, 'message': 'Invalid request method'}, status=405)


def remove_from_cart(request, item_id):
    """Remove item from cart"""
    cart_item = get_object_or_404(CartItem, id=item_id)
    cart = cart_item.cart
    cart_item.delete()
    
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({
            'success': True,
            'message': 'Item removed from cart',
            'cart_count': cart.item_count,
            'cart_total': float(cart.total_amount)
        })
    
    messages.success(request, 'Item removed from cart')
    return redirect('customer_interface:cart')


def cart_view(request):
    """Display shopping cart"""
    cart = get_or_create_cart(request)
    cart_items = cart.items.select_related('menu_item').all()
    
    context = {
        'cart': cart,
        'cart_items': cart_items,
    }
    return render(request, 'customer_interface/cart.html', context)


def checkout_view(request):
    """Checkout process"""
    cart = get_or_create_cart(request)
    cart_items = cart.items.select_related('menu_item').all()
    
    if not cart_items.exists():
        messages.warning(request, 'Your cart is empty')
        return redirect('customer_interface:menu')
    
    if request.method == 'POST':
        # Process checkout
        customer_name = request.POST.get('customer_name')
        customer_email = request.POST.get('customer_email')
        customer_phone = request.POST.get('customer_phone')
        order_type = request.POST.get('order_type', 'dine_in')
        table_number = request.POST.get('table_number')
        notes = request.POST.get('notes', '')
        
        # Create customer order
        order = CustomerOrder.objects.create(
            customer_name=customer_name,
            customer_email=customer_email,
            customer_phone=customer_phone,
            order_type=order_type,
            table_number=table_number if table_number else None,
            notes=notes,
            total_amount=cart.total_amount
        )
        
        # Create order items
        for cart_item in cart_items:
            CustomerOrderItem.objects.create(
                order=order,
                menu_item=cart_item.menu_item,
                quantity=cart_item.quantity,
                price_at_time=cart_item.menu_item.price
            )
        
        # Clear cart
        cart.delete()
        
        messages.success(request, f'Order placed successfully! Order number: {order.order_number}')
        return redirect('customer_interface:order_tracking', order_number=order.order_number)
    
    context = {
        'cart': cart,
        'cart_items': cart_items,
    }
    return render(request, 'customer_interface/checkout.html', context)


def order_tracking(request, order_number):
    """Order tracking page"""
    order = get_object_or_404(CustomerOrder, order_number=order_number)
    order_items = order.items.select_related('menu_item').all()
    
    # Status progress for the progress bar
    status_progress = {
        'pending': 0,
        'confirmed': 25,
        'preparing': 50,
        'ready': 75,
        'completed': 100,
        'cancelled': 0
    }
    
    context = {
        'order': order,
        'order_items': order_items,
        'status_progress': status_progress.get(order.status, 0),
    }
    return render(request, 'customer_interface/order_tracking.html', context)


def order_status_api(request, order_number):
    """API endpoint for real-time order status updates"""
    order = get_object_or_404(CustomerOrder, order_number=order_number)
    
    return JsonResponse({
        'order_number': order.order_number,
        'status': order.status,
        'status_display': order.get_status_display(),
        'updated_at': order.updated_at.isoformat(),
    })


def search_menu(request):
    """Search menu items"""
    query = request.GET.get('q', '')
    if query:
        menu_items = MenuItem.objects.filter(
            Q(name__icontains=query) | 
            Q(description__icontains=query),
            is_available=True
        ).select_related('category')
    else:
        menu_items = MenuItem.objects.filter(is_available=True).select_related('category')
    
    # Pagination
    paginator = Paginator(menu_items, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    cart = get_or_create_cart(request)
    
    context = {
        'menu_items': page_obj,
        'query': query,
        'cart': cart,
    }
    return render(request, 'customer_interface/search_results.html', context) 