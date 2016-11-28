from django.test import TestCase
from shop_app.models import Product, ProductOptions, Brand


# Create your tests here.
class TestBrand(TestCase):
    def test_brand_creation(self):
        brand_name = Brand.objects.create(brand_name='Brand new brand')
        assert brand_name is not None

    # @classmethod
    # def setUp(cls):
    #     pass


class TestProductOptions(TestCase):
    @classmethod
    def setUp(cls):
        pass
