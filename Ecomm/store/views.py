from django.shortcuts import render
from django.db.models import Prefetch
from .models import Product, Category
# Create your views here.

def homepage(request):
    categories = Category.objects.prefetch_related(Prefetch('products', queryset= Product.objects.only('id', 'image'), to_attr='related_images'))
    return render(request, 'store/home.html', {'categories': categories})

def category_products(request,category_id):
    category = Category.objects.get(id=category_id)
    products = Product.objects.filter(category=category)
    return render(request, 'store/category_products.html', {'category': category, 'products': products})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})

def about_us(request):
    return render(request, 'store/about_us.html')

def contact_us(request):
    return render(request, 'store/contact_us.html')