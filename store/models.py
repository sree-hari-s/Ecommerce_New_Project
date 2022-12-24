from django.db import models
from category.models import Category
from django.urls import reverse
# Create your models here.


class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(max_length=500, blank=True)
    price = models.IntegerField()
    images = models.ImageField(upload_to='photos/products')
    stock = models.IntegerField()
    is_available = models.BooleanField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.product_name
    
    def get_url(self):
        return reverse('product_detail',args=[self.category.slug,self.slug])
    
class VariationManager(models.Manager):
    def colors(self):
        return super(VariationManager,self).filter(variation_category='color',is_active=True)

    def size(self):
        return super(VariationManager,self).filter(variation_category='size',is_active=True)

class Variation(models.Model):
    variation_category_choice=(
        ('color','color'),
        ('size','size'),
    )
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    variation_category= models.CharField(max_length=100,choices=variation_category_choice)
    variation_value = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_date=models.DateTimeField(auto_now=True)
    
    objects=VariationManager()
    
    def __str__(self):
        return self.variation_value
    
class ProductGallery(models.Model):
    product = models.ForeignKey(Product,default=None,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='store/products',max_length=255)
    
    def __str__(self):
        return self.product.product_name
    
    class Meta:
        verbose_name='productgallery'
        verbose_name_plural = 'product gallery'
        
