from django.core.management.base import BaseCommand
from apps.inventory.models import Category, MenuItem


class Command(BaseCommand):
    help = 'Populate the database with sample menu categories and items'

    def handle(self, *args, **options):
        self.stdout.write('Creating sample menu data...')
        
        # Create categories
        categories_data = [
            {
                'name': 'Appetizers',
                'description': 'Start your meal with our delicious appetizers'
            },
            {
                'name': 'Soups',
                'description': 'Warm and comforting soups made with fresh ingredients'
            },
            {
                'name': 'Main Course',
                'description': 'Our signature main dishes prepared with care'
            },
            {
                'name': 'Desserts',
                'description': 'Sweet endings to your perfect meal'
            },
            {
                'name': 'Beverages',
                'description': 'Refreshing drinks and hot beverages'
            }
        ]
        
        categories = {}
        for cat_data in categories_data:
            category, created = Category.objects.get_or_create(
                name=cat_data['name'],
                defaults={'description': cat_data['description']}
            )
            categories[cat_data['name']] = category
            if created:
                self.stdout.write(f'Created category: {category.name}')
        
        # Create menu items
        menu_items_data = [
            # Appetizers
            {
                'name': 'Bruschetta',
                'category': 'Appetizers',
                'description': 'Toasted bread topped with fresh tomatoes, basil, and garlic',
                'price': 8.99,
                'stock_quantity': 50
            },
            {
                'name': 'Mozzarella Sticks',
                'category': 'Appetizers',
                'description': 'Crispy breaded mozzarella served with marinara sauce',
                'price': 7.99,
                'stock_quantity': 40
            },
            {
                'name': 'Spinach Artichoke Dip',
                'category': 'Appetizers',
                'description': 'Creamy dip with spinach, artichokes, and melted cheese',
                'price': 9.99,
                'stock_quantity': 30
            },
            
            # Soups
            {
                'name': 'Tomato Basil Soup',
                'category': 'Soups',
                'description': 'Rich tomato soup with fresh basil and cream',
                'price': 6.99,
                'stock_quantity': 60
            },
            {
                'name': 'Chicken Noodle Soup',
                'category': 'Soups',
                'description': 'Homestyle chicken soup with vegetables and egg noodles',
                'price': 7.99,
                'stock_quantity': 55
            },
            {
                'name': 'French Onion Soup',
                'category': 'Soups',
                'description': 'Classic French onion soup with melted cheese',
                'price': 8.99,
                'stock_quantity': 45
            },
            
            # Main Course
            {
                'name': 'Grilled Salmon',
                'category': 'Main Course',
                'description': 'Fresh Atlantic salmon grilled to perfection with herbs',
                'price': 24.99,
                'stock_quantity': 25
            },
            {
                'name': 'Beef Tenderloin',
                'category': 'Main Course',
                'description': 'Premium cut beef tenderloin with red wine reduction',
                'price': 29.99,
                'stock_quantity': 20
            },
            {
                'name': 'Chicken Marsala',
                'category': 'Main Course',
                'description': 'Pan-seared chicken in Marsala wine sauce with mushrooms',
                'price': 19.99,
                'stock_quantity': 35
            },
            {
                'name': 'Vegetarian Pasta',
                'category': 'Main Course',
                'description': 'Fresh pasta with seasonal vegetables and pesto sauce',
                'price': 16.99,
                'stock_quantity': 40
            },
            {
                'name': 'Ribeye Steak',
                'category': 'Main Course',
                'description': 'Juicy ribeye steak with garlic butter and herbs',
                'price': 32.99,
                'stock_quantity': 15
            },
            
            # Desserts
            {
                'name': 'Chocolate Lava Cake',
                'category': 'Desserts',
                'description': 'Warm chocolate cake with molten center, served with vanilla ice cream',
                'price': 8.99,
                'stock_quantity': 30
            },
            {
                'name': 'New York Cheesecake',
                'category': 'Desserts',
                'description': 'Classic New York style cheesecake with berry compote',
                'price': 7.99,
                'stock_quantity': 25
            },
            {
                'name': 'Tiramisu',
                'category': 'Desserts',
                'description': 'Italian dessert with coffee-soaked ladyfingers and mascarpone',
                'price': 9.99,
                'stock_quantity': 20
            },
            
            # Beverages
            {
                'name': 'Fresh Lemonade',
                'category': 'Beverages',
                'description': 'Homemade lemonade with fresh lemons and mint',
                'price': 4.99,
                'stock_quantity': 100
            },
            {
                'name': 'Iced Tea',
                'category': 'Beverages',
                'description': 'Refreshing iced tea with lemon',
                'price': 3.99,
                'stock_quantity': 80
            },
            {
                'name': 'Espresso',
                'category': 'Beverages',
                'description': 'Single shot of premium Italian espresso',
                'price': 3.49,
                'stock_quantity': 60
            },
            {
                'name': 'Cappuccino',
                'category': 'Beverages',
                'description': 'Espresso with steamed milk and foam',
                'price': 4.49,
                'stock_quantity': 70
            }
        ]
        
        for item_data in menu_items_data:
            menu_item, created = MenuItem.objects.get_or_create(
                name=item_data['name'],
                category=categories[item_data['category']],
                defaults={
                    'description': item_data['description'],
                    'price': item_data['price'],
                    'stock_quantity': item_data['stock_quantity'],
                    'is_available': True
                }
            )
            if created:
                self.stdout.write(f'Created menu item: {menu_item.name} - ${menu_item.price}')
        
        self.stdout.write(
            self.style.SUCCESS('Successfully populated menu with sample data!')
        )
        self.stdout.write(f'Created {len(categories)} categories and {len(menu_items_data)} menu items.') 