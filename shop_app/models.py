from django.db import models


# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=30)  # footwear, sportswear, jeans ...


class ProductOptions(models.Model):
    product_id = models.ForeignKey('Product')
    option_group_id = models.ForeignKey('OptionsGroups')  # 1 - color, 2 - size
    option_name = models.CharField(max_length=20)  # red, blue, M, S
    made_in = models.CharField(max_length=50)  # China, USA, Turkey ...
    fabrics = models.CharField(max_length=150)  # 87% wool, 10% polyamide, 3% elastane


class OptionsGroups(models.Model):
    option_group_name = models.CharField(max_length=30)  # color, size ...


class Brand(models.Model):
    brand_name = models.CharField(max_length=50)  # Nike, Adidas ...


class Product(models.Model):
    SKU = models.CharField(max_length=50)
    vendor_id = models.CharField(max_length=50)
    brand = models.ForeignKey('Brand')
    product_name = models.CharField(max_length=100)
    product_description_short = models.CharField(max_length=600)
    product_description_long = models.TextField()
    category_id = models.ForeignKey('Category')
    unit_price = models.DecimalField(max_digits=9, decimal_places=2)
    discount = models.DecimalField(max_digits=2, decimal_places=2)
    product_weight = models.DecimalField(max_digits=3, decimal_places=3)
    product_stock = models.PositiveSmallIntegerField()
    products_ordered = models.PositiveSmallIntegerField()
    product_available = models.BooleanField(default=True)
    discount_available = models.BooleanField()
    is_bestseller = models.BooleanField()
    product_image = models.URLField()








