from unicodedata import category
from django.db import models
from main.models import BaseModel
from versatileimagefield.fields import VersatileImageField

# Create your models here.

class Category(BaseModel):
    title = models.CharField(max_length=255)
    description_title = models.CharField(max_length=255)
    description = models.TextField()
    image = VersatileImageField('Image', upload_to="product/category")

    class Meta:
        db_table = 'product_category'
        verbose_name = ('Product Category')
        verbose_name_plural = ('Product Category')
        ordering = ('auto_id',)

    def __str__(self):
        return str(self.title)
    
    
class Product(BaseModel):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,limit_choices_to={'is_deleted': False})
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    image = VersatileImageField('Image', upload_to="product/product")

    class Meta:
        db_table = 'product_product'
        verbose_name = ('Product Product')
        verbose_name_plural = ('Product Product')
        ordering = ('auto_id',)

    def __str__(self):
        return str(self.name)