from django.db import models


# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=30, unique=True)  # footwear, sportswear, jeans ...

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_name


class OptionsGroups(models.Model):
    option_group_name = models.CharField(max_length=30, unique=True)  # color, size ...

    class Meta:
        verbose_name_plural = 'Options Groups'

    def __str__(self):
        return self.option_group_name


class Options(models.Model):
    option_group = models.ForeignKey('OptionsGroups')  # 1 - color, 2 - size
    option_name = models.CharField(max_length=20, unique=True)  # red, blue, M, S

    class Meta:
        verbose_name_plural = 'Options'

    def __str__(self):
        return self.option_name


class ProductOptions(models.Model):
    product = models.ForeignKey('Product')
    option_group = models.ForeignKey('OptionsGroups')
    option = models.ForeignKey('Options')

    class Meta:
        verbose_name_plural = 'Product Options'

    def __str__(self):

        return '{product} | {group} | {option}'.format(
            product=self.product,
            group=self.option_group,
            option=self.option,
        )


class Brand(models.Model):
    brand_name = models.CharField(max_length=50, unique=True)  # Nike, Adidas ...

    class Meta:
        verbose_name_plural = 'Brands'

    def __str__(self):
        return self.brand_name


class Product(models.Model):
    sku = models.CharField(max_length=50)
    # vendor_id = models.CharField(max_length=50, blank=True, default='')

    brand = models.ForeignKey('Brand')
    category = models.ForeignKey('Category')

    product_name = models.CharField(max_length=100)
    product_description_short = models.CharField(max_length=600)
    product_description_long = models.TextField(blank=True, default='')

    unit_price = models.DecimalField(max_digits=9, decimal_places=2)
    discount = models.DecimalField(max_digits=3, decimal_places=2, default=1.0,)
    discount_available = models.BooleanField()

    product_weight = models.DecimalField(max_digits=6, decimal_places=3, blank=True, default=0)
    product_stock = models.PositiveSmallIntegerField(default=0)
    products_ordered = models.PositiveSmallIntegerField(default=0)
    product_available = models.BooleanField(default=True)
    is_bestseller = models.BooleanField(default=False)

    product_image = models.ImageField(upload_to='media/products/', blank=True)

    made_in = models.CharField(max_length=50)  # China, USA, Turkey ...
    fabrics = models.CharField(max_length=100)  # 87% wool, 10% polyamide, 3% elastane

    class Meta:
        verbose_name_plural = 'Products'

    def __str__(self):
        return '{category} | {brand} | {product}'.format(
            category=self.category,
            brand=self.brand,
            product=self.product_name,
        )


class Images (models.Model):
    product = models.ForeignKey('Product')
    path = models.ImageField(upload_to='media/products/', blank=True)
    alt = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Images'


# class TestImage(models.Model):
#     image = models.ImageField(upload_to='/media/', blank=True)
