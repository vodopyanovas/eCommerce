# -*- coding: utf-8 -*-
from shop_app.cart import Cart
from shop_app.models import Item, Image

__author__ = 'Anton Vodopyanov'


def cart_item(request):
    images = Image.objects.all()
    cart_id = 4
    count_items = Item.objects.filter(cart_id=cart_id).count()
    get_items = Item.objects.filter(cart_id=cart_id)

    return {'quantity': count_items, 'items': get_items, 'images': images }

#
# def cart_item(request):
#     cart_id = 4
#     get_items = Item.objects.filter(cart_id=cart_id)
#