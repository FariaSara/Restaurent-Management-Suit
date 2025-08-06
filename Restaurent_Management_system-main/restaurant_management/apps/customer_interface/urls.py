from django.urls import path
from . import views

app_name = 'customer_interface'

urlpatterns = [
    # Menu and browsing
    path('', views.menu_view, name='menu'),
    path('search/', views.search_menu, name='search'),
    
    # Cart management
    path('cart/', views.cart_view, name='cart'),
    path('cart/add/', views.add_to_cart, name='add_to_cart'),
    path('cart/update/<int:item_id>/', views.update_cart_item, name='update_cart_item'),
    path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    
    # Checkout and orders
    path('checkout/', views.checkout_view, name='checkout'),
    path('order/<str:order_number>/', views.order_tracking, name='order_tracking'),
    path('api/order/<str:order_number>/status/', views.order_status_api, name='order_status_api'),
] 