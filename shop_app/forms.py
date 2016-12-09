# -*- coding: utf-8 -*-

from django import forms

from django.core.exceptions import ValidationError
# from django.utils.translation import ugettext_lazy as _

from shop_app.models import ProductOptions, Product, Brand, Category, OptionsGroups, Options, Subscriber, Country

__author__ = 'Anton Vodopyanov'


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = [
            'product_stock',
            'products_ordered',
            'product_available',
            'is_bestseller',
        ]


class ProductOptionsForm(forms.ModelForm):
    class Meta:
        model = ProductOptions
        fields = '__all__'


class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = '__all__'


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class OptionsGroupsForm(forms.ModelForm):
    class Meta:
        model = OptionsGroups
        fields = '__all__'


class OptionsForm(forms.ModelForm):
    class Meta:
        model = Options
        fields = '__all__'


class SubscriberForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Enter your Email'}))

    class Meta:
        model = Subscriber
        fields = '__all__'


class CountryForm(forms.ChoiceField):
    class Meta:
        model = Country
        fields = 'country_name'
