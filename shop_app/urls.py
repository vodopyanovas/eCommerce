# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.conf import settings
from django.views.static import serve

__author__ = 'Anton Vodopyanov'

from django.conf.urls import url, include
from django.contrib import admin

from shop_app.views import \
    index, product_attributes, products,\
    no_page, cart, checkout, wishlist, contact, product, product_detail, account


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'),
    url(r'^error/', no_page, name='no_page'),
    url(r'^cart/', cart, name='cart'),
    url(r'^checkout/', checkout, name='checkout'),
    url(r'^wishlist/', wishlist, name='wishlist'),
    url(r'^contact/', contact, name='contact'),
    url(r'^product/', product, name='product'),
    url(r'^product-detail/', product_detail, name='product_detail'),
    url(r'^account/', account, name='account'),
]

# if settings.DEBUG:
#     urlpatterns += [
#         url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }),
#    ]