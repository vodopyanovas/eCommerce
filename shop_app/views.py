from django.shortcuts import render
from django.http import HttpResponse, Http404

from shop_app.forms import ProductForm, ProductOptionsForm, BrandForm, CategoryForm, OptionsGroupsForm, OptionsForm, Country
from shop_app.models import Product, ProductOptions, Country, Image
from django.db import transaction


# Create your views here.
def index(request):
    if request.method == 'GET':
        # form = {
        #     'product_form': ProductForm(),
        #     'product_options': ProductOptionsForm(),
        #     # 'image': TestImageForm(),
        # }
        # return render(request, 'shop_app/index.html', form)
        return render(request, 'shop_app_2/index.html')

    elif request.method == 'POST':
        # product_form = ProductForm(request.POST)
        # options_form = ProductOptionsForm(request.POST)
        # # image = TestImageForm(request.POST)
        #
        # if product_form.is_valid():
        #     with transaction.atomic():
        #         product_form.save()
        #
        # elif options_form.is_valid():
        #     with transaction.atomic():
        #         options_form.save()

        # elif image.is_valid():
        #     with transaction.atomic():
        #         image.save()

        # form = {
        #     'product_form': ProductForm(),
        #     'product_options': ProductOptionsForm(),
        #     # 'image': TestImageForm(),
        # }
        #
        # return render(request, 'shop_app/index.html', form)
        return render(request, 'shop_app_2/index.html')

    return HttpResponse(status=405)


def no_page(request):
    if request.method == 'GET':
        return render(request, 'shop_app_2/404.html')

    elif request.method == 'POST':
        return render(request, 'shop_app_2/404.html')

    return HttpResponse(status=405)


def cart(request):
    if request.method == 'GET':
        return render(request, 'shop_app_2/cart.html')

    elif request.method == 'POST':
        return render(request, 'shop_app_2/cart.html')

    return HttpResponse(status=405)


def checkout(request):
    if request.method == 'GET':
        country = Country.objects.order_by('country_name')

        return render(request, 'shop_app_2/checkout.html', {'contr': country})

    elif request.method == 'POST':
        return render(request, 'shop_app_2/checkout.html')

    return HttpResponse(status=405)


def wishlist(request):
    if request.method == 'GET':
        return render(request, 'shop_app_2/wishlist.html')

    elif request.method == 'POST':
        return render(request, 'shop_app_2/wishlist.html')

    return HttpResponse(status=405)


def contact(request):
    if request.method == 'GET':
        return render(request, 'shop_app_2/contact.html')

    elif request.method == 'POST':
        return render(request, 'shop_app_2/contact.html')

    return HttpResponse(status=405)


def product(request):
    if request.method == 'GET':
        return render(request, 'shop_app_2/product.html')

    elif request.method == 'POST':
        return render(request, 'shop_app_2/product.html')

    return HttpResponse(status=405)


def product_detail(request):
    if request.method == 'GET':

        # images = Image.objects.all()

        return render(request, 'shop_app_2/product-detail.html',)

    elif request.method == 'POST':
        return render(request, 'shop_app_2/product-detail.html')

    return HttpResponse(status=405)


def account(request):
    if request.method == 'GET':
        return render(request, 'shop_app_2/account.html')

    elif request.method == 'POST':
        return render(request, 'shop_app_2/account.html')

    return HttpResponse(status=405)



def product_attributes(request):
    # if request.method == 'GET':
    #     form = {
    #         'brand': BrandForm(),
    #         'category': CategoryForm(),
    #         'options': OptionsForm,
    #         'options_groups': OptionsGroupsForm(),
    #     }
    #     return render(request, 'shop_app/attributes.html', form)
    #
    # elif request.method == 'POST':
    #
    #     brand_form = BrandForm(request.POST)
    #     category_form = CategoryForm(request.POST)
    #     options_form = OptionsForm(request.POST)
    #     options_groups_form = OptionsGroupsForm(request.POST)
    #
    #     if brand_form.is_valid():
    #         with transaction.atomic():
    #             brand_form.save()
    #
    #     elif category_form.is_valid():
    #         with transaction.atomic():
    #             category_form.save()
    #
    #     elif options_form.is_valid():
    #         with transaction.atomic():
    #             options_form.save()
    #
    #     elif options_groups_form.is_valid():
    #         with transaction.atomic():
    #             options_groups_form.save()
    #
    #     form = {
    #         'brand': BrandForm(),
    #         'category': CategoryForm(),
    #         'options': OptionsForm,
    #         'options_groups': OptionsGroupsForm(),
    #     }
    #     return render(request, 'shop_app/attributes.html', form)
    # return HttpResponse(status=405)
    pass


def products(request):
    # if request.method == 'GET':
    #     all_products = Product.objects.all()
    #
    #     all_options = ProductOptions.objects.all()
    #
    #     # group =
    #
    #     return render(request, 'shop_app/products.html', {'all_prod': all_products, 'all_opt': all_options})
    # return HttpResponse(status=405)
    pass
