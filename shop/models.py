from django.db import models
from .helpers import SaveMediaFiles, Choises
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(verbose_name='Slug', max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to=SaveMediaFiles.category_img_path)
    create_date = models.DateField(auto_now=True)
    last_update = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title

class Product(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField()
    image = models.ImageField(upload_to=SaveMediaFiles.product_img_path)
    category = models.ManyToManyField(Category)
    price = models.FloatField()
    price_type = models.CharField(max_length=10, choices=Choises.PriceType.choices, default=Choises.PriceType.s)
    category_code = models.CharField(verbose_name="Kategoriya kodi", max_length=200)
    category_name = models.CharField(verbose_name="Category Nomi", max_length=200)
    subcategory_code = models.CharField(verbose_name="Ost-kategoriya kodi", max_length=34)
    subcategory_name = models.CharField(verbose_name="Ost-kategoriya nomi", max_length=30)

    create_date = models.DateField(auto_now=True)
    last_update = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name 

class Cart(models.Model):
    title = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateField(auto_now=True)
    last_update = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title.name
    
class Testimonial(models.Model):
    full_name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to=SaveMediaFiles.testiminial_img_path)
    create_date = models.DateField(auto_now=True)
    last_update = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.full_name

    
