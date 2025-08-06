# 🍽️ Restaurant Management System

A complete Django-based restaurant management system with both customer interface and staff management capabilities.

## 🌟 Features

### Customer Interface
- **Menu Browsing**: Browse menu items organized by categories (Appetizers, Soups, Main Course, Desserts, Beverages)
- **Shopping Cart**: Add items, adjust quantities, remove items with real-time updates
- **Order Placement**: Simple checkout process with customer information
- **Order Tracking**: Real-time order status tracking with progress indicators
- **Order Types**: Support for both dine-in and takeaway orders
- **Search Functionality**: Search menu items with pagination

### Staff Management
- **Dashboard**: Comprehensive restaurant overview with statistics
- **Order Management**: View, update, and manage customer orders
- **Table Management**: Manage restaurant tables and reservations
- **Inventory Management**: Manage menu items and categories
- **Admin Panel**: Full administrative control over the system

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip (Python package installer)

### Installation

1. **Extract the project**
   ```bash
   unzip Restaurant_Management_System_Complete.zip
   cd restaurant_management
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows:
   venv\Scripts\activate
   
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Populate sample data**
   ```bash
   python manage.py populate_menu
   ```

6. **Create admin user (optional)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Start the development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   - Main URL: http://127.0.0.1:8000/
   - Customer Interface: http://127.0.0.1:8000/customer/
   - Admin Panel: http://127.0.0.1:8000/admin/

## 📁 Project Structure

```
restaurant_management/
├── apps/
│   ├── dashboard/          # Main dashboard and home page
│   ├── customer_interface/ # Customer-facing features
│   ├── inventory/          # Menu and inventory management
│   ├── orders/            # Order management system
│   └── tables/            # Table reservation system
├── core/                  # Django settings and configuration
├── templates/             # HTML templates
├── static/               # CSS, JS, and static files
├── media/                # User-uploaded files
└── manage.py             # Django management script
```

## 🎯 Key Features Explained

### Unified Interface
- **Single Landing Page**: Both customers and staff access the system from one URL
- **Role-Based Access**: Automatic redirection based on user type
- **Seamless Navigation**: Easy switching between customer and staff areas

### Customer Experience
- **Responsive Design**: Works on desktop, tablet, and mobile devices
- **Real-time Updates**: Live cart updates and order status tracking
- **User-Friendly**: Intuitive interface with clear navigation

### Staff Management
- **Comprehensive Dashboard**: Overview of orders, tables, and menu items
- **Order Processing**: Update order statuses in real-time
- **Inventory Control**: Manage menu items and categories
- **Table Management**: Handle reservations and table assignments

## 🔧 Configuration

### Environment Variables
Create a `.env` file in the project root:
```
DEBUG=True
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///db.sqlite3
```

### Database
The system uses SQLite by default. For production, consider using PostgreSQL or MySQL.

## 📱 Usage

### For Customers
1. Visit http://127.0.0.1:8000/
2. Click "Browse Menu & Order"
3. Browse menu items by category
4. Add items to cart
5. Proceed to checkout
6. Track your order status

### For Staff
1. Visit http://127.0.0.1:8000/
2. Click "Staff Login"
3. Log in with admin credentials
4. Access dashboard and management tools
5. Update order statuses and manage inventory

## 🛠️ Customization

### Adding Menu Items
1. Access the admin panel
2. Go to Inventory > Menu Items
3. Add new items with categories, prices, and descriptions

### Modifying Categories
1. Access the admin panel
2. Go to Inventory > Categories
3. Add or modify food categories

### Customizing Styles
- Edit CSS files in `static/css/`
- Modify Bootstrap classes in templates
- Update color schemes and branding

## 🔒 Security Features

- CSRF protection on all forms
- Session-based authentication
- Input validation and sanitization
- Secure file upload handling

## 📊 Database Models

### Customer Interface
- `Cart`: Shopping cart for anonymous users
- `CartItem`: Individual items in cart
- `CustomerOrder`: Customer orders
- `CustomerOrderItem`: Items in customer orders

### Staff Management
- `Order`: Staff-managed orders
- `OrderItem`: Items in staff orders
- `Table`: Restaurant tables
- `MenuItem`: Menu items
- `Category`: Food categories

## 🚀 Deployment

### Production Setup
1. Set `DEBUG=False` in settings
2. Configure production database
3. Set up static file serving
4. Configure web server (nginx, Apache)
5. Use production WSGI server (gunicorn, uwsgi)

### Docker Deployment
```bash
docker build -t restaurant-management .
docker run -p 8000:8000 restaurant-management
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

For support and questions:
- Check the documentation
- Review the code comments
- Create an issue on GitHub

## 🎉 Acknowledgments

- Django Framework
- Bootstrap 5
- Font Awesome Icons
- SQLite Database

---

**Enjoy your Restaurant Management System!** 🍽️✨ 