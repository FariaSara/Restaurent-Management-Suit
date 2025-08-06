# Customer Interface - Restaurant Management System

## Overview

The Customer Interface is a comprehensive web-based ordering system that allows customers to browse the restaurant menu, add items to their cart, place orders, and track their order status in real-time.

## Features

### 1. Menu Browsing
- **Category Organization**: Menu items are organized by categories (Appetizers, Soups, Main Course, Desserts, Beverages)
- **Search Functionality**: Customers can search for specific dishes or ingredients
- **Responsive Design**: Mobile-friendly interface that works on all devices
- **Item Details**: Each menu item displays:
  - High-quality images
  - Detailed descriptions
  - Pricing information
  - Category labels

### 2. Shopping Cart
- **Real-time Updates**: Cart updates instantly when items are added/removed
- **Quantity Controls**: Easy +/- buttons to adjust quantities
- **Item Management**: Remove items or update quantities
- **Cart Summary**: Shows total items and total amount
- **Session-based**: Cart persists during the customer's session

### 3. Order Placement
- **Simple Checkout**: Streamlined checkout process
- **Customer Information**: Collects name, email, and phone number
- **Order Types**: Supports both dine-in and takeaway orders
- **Table Numbers**: For dine-in orders, customers specify their table
- **Special Instructions**: Space for dietary requirements or special requests
- **Order Summary**: Clear breakdown of items and total cost

### 4. Order Tracking
- **Real-time Status**: Live updates of order status
- **Progress Indicators**: Visual progress bar showing order stages
- **Status Stages**:
  - Pending
  - Confirmed
  - Preparing
  - Ready
  - Completed
- **Order Details**: Complete order information and item breakdown
- **Contact Information**: Easy access to restaurant contact details

### 5. Order Types
- **Dine-in Orders**: For customers eating at the restaurant
- **Takeaway Orders**: For customers picking up their food
- **Flexible Options**: Easy switching between order types

## Technical Implementation

### Models
- **Cart**: Manages shopping cart sessions
- **CartItem**: Individual items in the cart
- **CustomerOrder**: Customer order information
- **CustomerOrderItem**: Individual items in customer orders

### Views
- **Menu View**: Displays menu organized by categories
- **Cart View**: Shopping cart management
- **Checkout View**: Order placement process
- **Order Tracking**: Real-time order status
- **Search View**: Menu item search functionality

### Templates
- **Base Template**: Common layout and styling
- **Menu Template**: Category-based menu display
- **Cart Template**: Shopping cart interface
- **Checkout Template**: Order placement form
- **Order Tracking Template**: Status tracking interface
- **Search Results Template**: Search functionality

### JavaScript Features
- **AJAX Cart Updates**: Real-time cart modifications
- **Quantity Controls**: Interactive quantity adjustment
- **Toast Notifications**: User feedback for actions
- **Real-time Status Updates**: Automatic order status polling
- **Form Validation**: Client-side validation for checkout

## Installation and Setup

### 1. Database Migration
```bash
python manage.py makemigrations
python manage.py migrate
```

### 2. Populate Sample Data
```bash
python manage.py populate_menu
```

### 3. Create Admin User
```bash
python manage.py createsuperuser
```

### 4. Run Development Server
```bash
python manage.py runserver
```

## Usage

### Customer Flow
1. **Browse Menu**: Visit `/customer/` to view the menu
2. **Add to Cart**: Click "Add to Cart" on desired items
3. **View Cart**: Click cart icon to review items
4. **Checkout**: Proceed to checkout and fill in details
5. **Place Order**: Submit order and receive order number
6. **Track Order**: Monitor order status in real-time

### Admin Management
1. **Access Admin**: Visit `/admin/` and login
2. **Manage Orders**: View and update customer orders
3. **Update Status**: Change order status as it progresses
4. **View Analytics**: Monitor order patterns and customer data

## URL Structure

- `/customer/` - Main menu page
- `/customer/search/` - Search functionality
- `/customer/cart/` - Shopping cart
- `/customer/checkout/` - Order placement
- `/customer/order/<order_number>/` - Order tracking
- `/customer/api/order/<order_number>/status/` - Order status API

## Customization

### Styling
The interface uses Bootstrap 5 with custom CSS variables for easy theming:
- Primary color: `#d4af37` (Gold)
- Secondary color: `#2c3e50` (Dark Blue)
- Accent color: `#e74c3c` (Red)

### Adding Categories
1. Access Django admin
2. Go to Inventory > Categories
3. Add new category with name and description

### Adding Menu Items
1. Access Django admin
2. Go to Inventory > Menu items
3. Add new item with:
   - Name and description
   - Category selection
   - Price and stock quantity
   - Optional image upload

## Features in Detail

### Menu Browsing
- **Category Headers**: Each category has a distinctive header with description
- **Item Cards**: Clean card layout with images, descriptions, and pricing
- **Quantity Controls**: Built-in quantity adjustment before adding to cart
- **Responsive Grid**: Automatically adjusts layout for different screen sizes

### Shopping Cart
- **Real-time Updates**: No page refresh needed for cart modifications
- **Quantity Adjustment**: +/- buttons and direct input for quantities
- **Item Removal**: Easy removal of unwanted items
- **Total Calculation**: Automatic calculation of subtotals and totals
- **Empty State**: Helpful message when cart is empty

### Checkout Process
- **Form Validation**: Client and server-side validation
- **Order Type Selection**: Toggle between dine-in and takeaway
- **Table Number**: Required field for dine-in orders
- **Special Instructions**: Text area for dietary requirements
- **Order Summary**: Clear breakdown of all items and costs
- **Terms Agreement**: Required checkbox for order placement

### Order Tracking
- **Progress Bar**: Visual representation of order progress
- **Status Steps**: Clear indicators for each order stage
- **Real-time Updates**: Automatic status polling every 30 seconds
- **Order Details**: Complete order information display
- **Contact Information**: Easy access to restaurant contact details

## Security Features

- **CSRF Protection**: All forms include CSRF tokens
- **Session Management**: Secure cart session handling
- **Input Validation**: Server-side validation of all inputs
- **SQL Injection Protection**: Django ORM prevents SQL injection
- **XSS Protection**: Template escaping prevents XSS attacks

## Performance Optimizations

- **Database Queries**: Optimized queries with select_related and prefetch_related
- **Caching**: Session-based cart caching
- **Image Optimization**: Responsive images with proper sizing
- **JavaScript**: Efficient AJAX calls with error handling
- **Pagination**: Search results are paginated for better performance

## Future Enhancements

- **User Accounts**: Customer registration and login
- **Order History**: Past order tracking for registered users
- **Payment Integration**: Online payment processing
- **Loyalty Program**: Points and rewards system
- **Reviews and Ratings**: Customer feedback system
- **Mobile App**: Native mobile application
- **Push Notifications**: Real-time order updates
- **Analytics Dashboard**: Detailed order analytics

## Support

For technical support or questions about the customer interface:
- Check the Django admin panel for order management
- Review the console logs for any JavaScript errors
- Ensure all migrations have been applied
- Verify that sample data has been populated

## License

This customer interface is part of the Restaurant Management System and follows the same licensing terms. 