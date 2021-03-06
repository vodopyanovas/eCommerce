from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.http import HttpResponse, Http404

from shop_app.forms import SubscriberForm
from shop_auth_app.forms import CustomAuthenticationForm
from shop_app.models import Product, ProductOptions, Country, Image, Category, Item, Brand
from shop_app.cart import Cart
from django.db import transaction


# Create your views here.
def index(request):
    if request.method == 'GET':

        brands = Brand.objects.all().order_by('brand_name')
        latest_products = Product.objects.all().order_by('-product_add_date')

        return render(request, 'shop_app_2/index.html', {
            'latest': latest_products,
            'form': CustomAuthenticationForm,
            'brands': brands,
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


def add_to_cart(request, product_id, quantity):
    product_cart = Product.objects.get(id=product_id)
    cart = Cart(request)
    cart.add(product_cart, product_cart.unit_price, quantity)
    return HttpResponse("Item {product_cart} added to cart".format(product_cart=product_cart))
    # return redirect('shop_app_2/product.html')


def remove_from_cart(request, product_id):
    product_cart = Product.objects.get(id=product_id)
    cart = Cart(request)
    cart.remove(product_cart)
    return HttpResponse("Item {product_cart} removed!".format(product_cart=product_cart))


def get_cart(request):
    images = Image.objects.all()
    cart = Cart(request)

    return render(request, 'shop_app_2/cart.html', {
        'cart': cart,
        'images': images,
    })


@login_required
def checkout(request):
    if request.method == 'GET':
        country = Country.objects.order_by('country_name')
        cart = Cart(request)

        return render(request, 'shop_app_2/checkout.html', {
            'country': country,
            'cart': cart
        })

    elif request.method == 'POST':
        return render(request, 'shop_app_2/checkout.html')

    return HttpResponse(status=405)

@login_required()
def wishlist(request):
    if request.method == 'GET':
        return render(request, 'shop_app_2/wishlist.html')

    elif request.method == 'POST':
        return render(request, 'shop_app_2/wishlist.html')

    return HttpResponse(status=405)


def product(request):
    if request.method == 'GET':
        all_products = Product.objects.all().order_by('pk')
        categories = Category.objects.all()
        images = Image.objects.all().order_by('product')

        return render(request, 'shop_app_2/product.html', {
            'products': all_products,
            'categories': categories,
            'images': images,
        })

    elif request.method == 'POST':
        return render(request, 'shop_app_2/product.html')

    return HttpResponse(status=405)


def product_detail(request, product_id):
    if request.method == 'GET':

        get_product = get_object_or_404(Product, pk=product_id)

        img = Image.objects.all().filter(product_id=product_id,).first()

        # get_options = ProductOptions.objects.filter(product_id=product_id)
        # size = get_options.filter(option__option_group=2)
        # color = get_options.filter(option__option_group=1)
        color = ProductOptions.objects.select_related('option__option_group').filter(option_group=1)
        product_color = color.filter(product_id=product_id)
        size = ProductOptions.objects.select_related('option__option_group').filter(option_group=2)
        product_size = size.filter(product_id=product_id)

        return render(request, 'shop_app_2/product-detail.html', {
            'image': img,
            'product': get_product,
            'sizes': product_size,
            'colors': product_color,
        })

    elif request.method == 'POST':
        return render(request, 'shop_app_2/product-detail.html')

    return HttpResponse(status=405)

@login_required()
def account(request):
    if request.method == 'GET':
        form = CustomAuthenticationForm()
        return render(request, 'shop_app_2/account.html', {'form': form})

    elif request.method == 'POST':
        return render(request, 'shop_auth_app/login.html')
    return HttpResponse(status=405)


def contact(request):
    if request.method == 'GET':
        return render(request, 'shop_app_2/contact.html')

    elif request.method == 'POST':
        return render(request, 'shop_app_2/contact.html')

    return HttpResponse(status=405)


def no_page(request):
    if request.method == 'GET':
        return render(request, 'shop_app_2/404.html')

    elif request.method == 'POST':
        return render(request, 'shop_app_2/404.html')

    return HttpResponse(status=405)


# def subscribe(request):
#     # if request.method == 'GET':
#     #     return render(request, 'shop_app_2/contact.html')
#
#     if request.method == 'POST':
#         subs_form = SubscriberForm(request.POST)
#
#         if subs_form.is_valid():
#             with transaction.atomic():
#                 subs_form.save()
#
#         # my_form = {'subscribe_form': SubscriberForm()}
#
#         return render(request, 'shop_app_2/index.html',)
#
#     return HttpResponse(status=405)
