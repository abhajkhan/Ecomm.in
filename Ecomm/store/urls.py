from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('products/', views.product_list, name='product_list'),
    path('about_us/', views.about_us, name='about_us'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('category/<int:category_id>/', views.category_products, name='category_products'),

]
