from django.core.management.base import BaseCommand
from store.models import Category, Product

class Command(BaseCommand):
    help = 'Seed the database with sample categories and products'

    def handle(self, *args, **kwargs):
        # Create Categories
        categories = [
            {"category": "Electronics", "description": "Latest gadgets and devices to make your life smarter and more connected."},
            {"category": "Fashion", "description": "Trendy apparel and accessories to match your style."},
            {"category": "Home & Kitchen", "description": "Essentials and decor to create a cozy and functional living space."},
            {"category": "Books", "description": "A wide range of literature to spark your imagination and knowledge."},
            {"category": "Sports", "description": "Gear and equipment to support your active and healthy lifestyle."},
        ]

        for category_data in categories:
            category, created = Category.objects.get_or_create(category=category_data["category"], description=category_data["description"])
            if created:
                self.stdout.write(self.style.SUCCESS(f"Category '{category_data['category']}' created."))

        # Create Products
        products = [
            {"title": "Smartphone", "description": "A high-end smartphone with a sleek design and powerful features.", "price": 20000, "category_name": "Electronics"},
            {"title": "T-Shirt", "description": "A comfortable cotton t-shirt in various sizes and colors.", "price": 500, "category_name": "Fashion"},
            {"title": "Cookware Set", "description": "A premium cookware set to elevate your kitchen experience.", "price": 1500, "category_name": "Home & Kitchen"},
            {"title": "Novel", "description": "A captivating novel that keeps you on the edge of your seat.", "price": 300, "category_name": "Books"},
            {"title": "Football", "description": "A durable football for both casual play and professional training.", "price": 800, "category_name": "Sports"},
        ]

        for product_data in products:
            category = Category.objects.get(category=product_data["category_name"])
            product, created = Product.objects.get_or_create(
                title=product_data["title"],
                description=product_data["description"],
                price=product_data["price"],
                category=category
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Product '{product_data['title']}' created."))
