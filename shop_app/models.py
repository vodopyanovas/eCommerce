from django.db import models


# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=30)  # footwear, sportswear, jeans ...

    def __str__(self):
        return self.category_name


class OptionsGroups(models.Model):
    option_group_name = models.CharField(max_length=30)  # color, size ...

    def __str__(self):
        return self.option_group_name


class Options(models.Model):
    option_group_id = models.ForeignKey('OptionsGroups')  # 1 - color, 2 - size
    option_name = models.CharField(max_length=20)  # red, blue, M, S

    def __str__(self):
        return self.option_name


class ProductOptions(models.Model):
    product_id = models.ForeignKey('Product')
    option_group_id = models.ForeignKey('OptionsGroups')
    option_id = models.ForeignKey('Options')


class Brand(models.Model):
    brand_name = models.CharField(max_length=50)  # Nike, Adidas ...

    def __str__(self):
        return self.brand_name


class Product(models.Model):
    SKU = models.CharField(max_length=50)
    vendor_id = models.CharField(max_length=50, blank=True)
    brand = models.ForeignKey('Brand')
    category_id = models.ForeignKey('Category')
    product_name = models.CharField(max_length=100)
    product_description_short = models.CharField(max_length=600)
    product_description_long = models.TextField(blank=True)
    unit_price = models.DecimalField(max_digits=9, decimal_places=2)
    discount = models.DecimalField(max_digits=3, decimal_places=2, default=1.0,)
    product_weight = models.DecimalField(max_digits=6, decimal_places=3, blank=True)
    product_stock = models.PositiveSmallIntegerField(default=0)
    products_ordered = models.PositiveSmallIntegerField(default=0)
    product_available = models.BooleanField(default=True)
    discount_available = models.BooleanField()
    is_bestseller = models.BooleanField(default=False)
    product_image = models.ImageField(upload_to=None, blank=True)
    made_in = models.CharField(max_length=50)  # China, USA, Turkey ...
    fabrics = models.CharField(max_length=100)  # 87% wool, 10% polyamide, 3% elastane

    def __str__(self):
        return self.product_name








