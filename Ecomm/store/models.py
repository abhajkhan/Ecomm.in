from django.db import models

# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=225)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.category
    

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='product_images/')
    category = models.ForeignKey(Category,on_delete=models.CASCADE, related_name="products")

    def __str__(self) :
        return self.title
    
