from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404

# from shop_app.forms import *
from shop_app.models import Product, ProductOptions, Country, Image
from shop_app.cart import Cart
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
        latest_products = Product.objects.all().order_by('product_add_date')

        return render(request, 'shop_app_2/index.html', {
            'latest': latest_products,
        })

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

        return render(request, 'shop_app_2/checkout.html', {'country': country})

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

        img = Image.objects.all().filter(product_id=3,)

        get_product = Product.objects.get(pk=3)
        get_options = ProductOptions.objects.filter(product_id=3)
        size = get_options.filter(option__option_group=2)
        color = get_options.filter(option__option_group=1)

        return render(request, 'shop_app_2/product-detail.html', {
            'image': img,
            'product': get_product,
            'sizes': size,
            'colors': color,
        })

    elif request.method == 'POST':
        return render(request, 'shop_app_2/product-detail.html')

    return HttpResponse(status=405)


def account(request):
    if request.method == 'GET':
        return render(request, 'shop_app_2/account.html')

    elif request.method == 'POST':
        return render(request, 'shop_app_2/account.html')

    return HttpResponse(status=405)


def add_to_cart(request, product_id, quantity):
    product = Product.objects.get(id=product_id)
    cart = Cart(request)
    cart.add(product, product.unit_price, quantity)

def remove_from_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart = Cart(request)
    cart.remove(product)

def get_cart(request):
    return render_to_response('shop_app_2/cart.html', dict(cart=Cart(request)))


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
