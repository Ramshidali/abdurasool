from django import template
from product.models import Category,Product

register = template.Library()

@register.simple_tag
def get_product(category):
        if Product.objects.filter(category__pk=category,is_deleted=False).exists():
            product_instance = Product.objects.filter(category__pk=category,is_deleted=False)
            return product_instance
        else:
            return 1
