from django.shortcuts import render
from django.http import HttpResponse, Http404

from shop_app.forms import ProductForm, ProductOptionsForm, BrandForm, CategoryForm, OptionsGroupsForm, OptionsForm
from django.db import transaction


# Create your views here.
def index(request):
    if request.method == 'GET':
        form = {
            'product_form': ProductForm(),
            'product_options': ProductOptionsForm(),
        }
        return render(request, 'shop_app/index.html', form)

    elif request.method == 'POST':
        product_form = ProductForm(request.POST)
        options_form = ProductOptionsForm(request.POST)

        if product_form.is_valid():
            with transaction.atomic():
                product_form.save()

        elif options_form.is_valid():
            with transaction.atomic():
                options_form.save()

        form = {
            'product_form': ProductForm(),
            'product_options': ProductOptionsForm(),
        }

        return render(request, 'shop_app/index.html', form)

    return HttpResponse(status=405)


def product_attributes(request):
    if request.method == 'GET':
        form = {
            'brand': BrandForm(),
            'category': CategoryForm(),
            'options': OptionsForm,
            'options_groups': OptionsGroupsForm(),
        }
        return render(request, 'shop_app/attributes.html', form)

    elif request.method == 'POST':

        brand_form = BrandForm(request.POST)
        category_form = CategoryForm(request.POST)
        options_form = OptionsForm(request.POST)
        options_groups_form = OptionsGroupsForm(request.POST)

        if brand_form.is_valid():
            with transaction.atomic():
                brand_form.save()

        elif category_form.is_valid():
            with transaction.atomic():
                category_form.save()

        elif options_form.is_valid():
            with transaction.atomic():
                options_form.save()

        elif options_groups_form.is_valid():
            with transaction.atomic():
                options_groups_form.save()

        form = {
            'brand': BrandForm(),
            'category': CategoryForm(),
            'options': OptionsForm,
            'options_groups': OptionsGroupsForm(),
        }
        return render(request, 'shop_app/attributes.html', form)
    return HttpResponse(status=405)

