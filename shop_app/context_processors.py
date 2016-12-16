# -*- coding: utf-8 -*-
from shop_app.cart import Cart
from shop_app.models import Item

__author__ = 'Anton Vodopyanov'


def item_counter(request):
    cart_id = 4
    get_items = Item.objects.filter(cart_id=cart_id).count()
    return {'quantity': get_items}
