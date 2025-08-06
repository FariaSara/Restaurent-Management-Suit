from django.contrib import admin
from .models import Cart, CartItem, CustomerOrder, CustomerOrderItem


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['session_key', 'item_count', 'total_amount', 'created_at']
    list_filter = ['created_at']
    search_fields = ['session_key']
    readonly_fields = ['created_at', 'updated_at']
    
    def item_count(self, obj):
        return obj.item_count
    item_count.short_description = 'Items'
    
    def total_amount(self, obj):
        return f"${obj.total_amount}"
    total_amount.short_description = 'Total'


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['cart', 'menu_item', 'quantity', 'subtotal']
    list_filter = ['added_at', 'menu_item__category']
    search_fields = ['menu_item__name', 'cart__session_key']
    readonly_fields = ['added_at']
    
    def subtotal(self, obj):
        return f"${obj.subtotal}"
    subtotal.short_description = 'Subtotal'


@admin.register(CustomerOrder)
class CustomerOrderAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'customer_name', 'order_type', 'status', 'total_amount', 'created_at']
    list_filter = ['status', 'order_type', 'created_at']
    search_fields = ['order_number', 'customer_name', 'customer_email', 'customer_phone']
    readonly_fields = ['order_number', 'created_at', 'updated_at']
    list_editable = ['status']
    
    fieldsets = (
        ('Order Information', {
            'fields': ('order_number', 'status', 'order_type', 'total_amount')
        }),
        ('Customer Information', {
            'fields': ('customer_name', 'customer_email', 'customer_phone', 'table_number')
        }),
        ('Order Details', {
            'fields': ('notes', 'created_at', 'updated_at')
        }),
    )
    
    def total_amount(self, obj):
        return f"${obj.total_amount}"
    total_amount.short_description = 'Total'
    
    actions = ['mark_as_confirmed', 'mark_as_preparing', 'mark_as_ready', 'mark_as_completed']
    
    def mark_as_confirmed(self, request, queryset):
        updated = queryset.update(status='confirmed')
        self.message_user(request, f'{updated} order(s) marked as confirmed.')
    mark_as_confirmed.short_description = "Mark selected orders as confirmed"
    
    def mark_as_preparing(self, request, queryset):
        updated = queryset.update(status='preparing')
        self.message_user(request, f'{updated} order(s) marked as preparing.')
    mark_as_preparing.short_description = "Mark selected orders as preparing"
    
    def mark_as_ready(self, request, queryset):
        updated = queryset.update(status='ready')
        self.message_user(request, f'{updated} order(s) marked as ready.')
    mark_as_ready.short_description = "Mark selected orders as ready"
    
    def mark_as_completed(self, request, queryset):
        updated = queryset.update(status='completed')
        self.message_user(request, f'{updated} order(s) marked as completed.')
    mark_as_completed.short_description = "Mark selected orders as completed"


@admin.register(CustomerOrderItem)
class CustomerOrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'menu_item', 'quantity', 'price_at_time', 'subtotal']
    list_filter = ['menu_item__category']
    search_fields = ['order__order_number', 'menu_item__name']
    readonly_fields = ['subtotal']
    
    def subtotal(self, obj):
        return f"${obj.subtotal}"
    subtotal.short_description = 'Subtotal' 