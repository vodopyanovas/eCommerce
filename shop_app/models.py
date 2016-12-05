import os
from django.db import models
from datetime import date
from django.utils import timezone
from eCommerce.settings import MEDIA_ROOT
from django.contrib.contenttypes.models import ContentType

TODAY = date.today()
TODAY_PATH = TODAY.strftime("%Y/%m-%d")


# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=30, unique=True)  # footwear, sportswear, jeans ...

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str_(self):
        return self.category_name


class OptionsGroups(models.Model):
    option_group_name = models.CharField(max_length=30, unique=True)  # color, size ...

    class Meta:
        verbose_name_plural = 'Options Groups'

    def __str_(self):
        return self.option_group_name


class Options(models.Model):
    option_group = models.ForeignKey('OptionsGroups')  # 1 - color, 2 - size
    option_name = models.CharField(max_length=20, unique=True)  # red, blue, M, S

    class Meta:
        verbose_name_plural = 'Options'

    def __str_(self):
        return self.option_name


class ProductOptions(models.Model):
    product = models.ForeignKey('Product')
    option_group = models.ForeignKey('OptionsGroups')
    option = models.ForeignKey('Options')

    class Meta:
        verbose_name_plural = 'Product Options'

    def __str_(self):
        return '{product} | {group} | {option}'.format(
            product=self.product,
            group=self.option_group,
            option=self.option,
        )


def upload_brand_img(instance, filename):  # shop_app/media/brand-logo
    return os.path.join(MEDIA_ROOT, 'brand-logo', TODAY_PATH, str(instance.brand_name), filename)

class Brand(models.Model):
    brand_name = models.CharField(max_length=50, unique=True)  # Nike, Adidas ...
    brand_logo = models.ImageField(upload_to=upload_brand_img, blank=True)

    class Meta:
        verbose_name_plural = 'Brands'

    def __str_(self):
        return self.brand_name


class Product(models.Model):
    GENDER_CHOICE = (
        ('M', 'Male',),
        ('F', 'Female',),
        ('Uni', 'Unisex',),
    )

    sku = models.CharField(max_length=50)
    # vendor_id = models.CharField(max_length=50, blank=True, default='')
    gender = models.CharField(max_length=3, choices=GENDER_CHOICE, blank=True)
    brand = models.ForeignKey('Brand')
    category = models.ForeignKey('Category')

    product_name = models.CharField(max_length=100)
    product_description_short = models.CharField(max_length=600)
    product_description_long = models.TextField(blank=True, default='')

    unit_price = models.DecimalField(max_digits=9, decimal_places=2)
    discount = models.DecimalField(max_digits=3, decimal_places=2, default=1.0, )
    discount_available = models.BooleanField()

    product_weight = models.DecimalField(max_digits=6, decimal_places=3, blank=True, default=0)
    product_stock = models.PositiveSmallIntegerField(default=0)
    products_ordered = models.PositiveSmallIntegerField(default=0)
    product_available = models.BooleanField(default=True)
    is_bestseller = models.BooleanField(default=False)

    # product_image = models.ImageField(upload_to='media/products/', blank=True)

    made_in = models.ForeignKey('Country')  # China, USA, Turkey ...
    fabrics = models.CharField(max_length=100)  # 87% wool, 10% polyamide, 3% elastane
    product_add_date = models.DateTimeField(default=timezone.now, )

    class Meta:
        verbose_name_plural = 'Products'

    def __str_(self):
        return '{category}/{brand}/{product}'.format(
            category=self.category,
            brand=self.brand,
            product=self.product_name,
        )


def upload_large_img(instance, filename):  # /shop_app/media/view-slider/large/2016/12-01/Outwear/Woolrich/Arctic DF Melton Blue/woolrich-arctic_large.jpg
    return os.path.join(MEDIA_ROOT, 'view-slider', 'large', TODAY_PATH, str(instance.product), filename)

def upload_medium_img(instance, filename):  # /shop_app/media/view-slider/medium/2016/12-01/Outwear/Woolrich/Arctic DF Melton Blue/woolrich-arctic_medium.jpg
    return os.path.join(MEDIA_ROOT, 'view-slider', 'medium', TODAY_PATH, str(instance.product), filename)

def upload_thubm_img(instance, filename):  # shop_app/media/view-slider/thumbnail/2016/12-01/Outwear/Woolrich/Arctic DF Melton Blue/woolrich-arctic_thumb.jpg
    return os.path.join(MEDIA_ROOT, 'view-slider', 'thumbnail', TODAY_PATH, str(instance.product), filename)


class Image(models.Model):
    product = models.ForeignKey('Product')
    large = models.ImageField(upload_to=upload_large_img, blank=True, max_length=300)
    medium = models.ImageField(upload_to=upload_medium_img, blank=True, max_length=300)
    thumbnail = models.ImageField(upload_to=upload_thubm_img, blank=True, max_length=300)
    alt = models.CharField(max_length=50)
    image_add_date = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = 'Images'

    def __str_(self):
        return self.product


class Country(models.Model):
    country_name = models.CharField(max_length=30, )

    class Meta:
        verbose_name_plural = 'Countries'
        ordering = ('country_name',)

    def __str_(self):
        return self.country_name


class Subscriber(models.Model):
    email = models.CharField(max_length=50)


# Cart models
class Cart(models.Model):
    creation_date = models.DateTimeField(verbose_name=('creation date'))
    checked_out = models.BooleanField(default=False, verbose_name=('checked out'))

    class Meta:
        verbose_name = ('cart')
        verbose_name_plural = ('carts')
        ordering = ('-creation_date',)

    def __str__(self):
        return self.creation_date


class ItemManager(models.Manager):
    def get(self, *args, **kwargs):
        if 'product' in kwargs:
            kwargs['content_type'] = ContentType.objects.get_for_model(type(kwargs['product']))
            kwargs['object_id'] = kwargs['product'].pk
            del(kwargs['product'])
        return super(ItemManager, self).get(*args, **kwargs)


class Item(models.Model):
    cart = models.ForeignKey(Cart, verbose_name=('cart'))
    quantity = models.PositiveIntegerField(verbose_name=('quantity'))
    unit_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name=('unit price'))
    # product as generic relation
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()

    objects = ItemManager()

    class Meta:
        verbose_name = ('item')
        verbose_name_plural = ('items')
        ordering = ('cart',)

    def __str__(self):
        return '{quantity} units of {product}'.format(quantity=self.quantity, product=self.product.__class__.__name__)

    def total_price(self):
        return self.quantity * self.unit_price
    total_price = property(total_price)

    # product
    def get_product(self):
        return self.content_type.get_object_for_this_type(pk=self.object_id)

    def set_product(self, product):
        self.content_type = ContentType.objects.get_for_model(type(product))
        self.object_id = product.pk

    product = property(get_product, set_product)
