# -*- coding: utf-8 -*-

# __author__ = 'Anton Vodopyanov'
from django.conf.urls import url
from django.contrib.auth.views import login, logout
from shop_auth_app.forms import CustomAuthenticationForm, UserCreationForm
# from shop_auth_app.views import register_user, register_success

urlpatterns = [
    url(r'^login/', login,
        {'template_name': 'shop_auth_app/login.html', 'authentication_form': CustomAuthenticationForm},
        name='login', ),
    url(r'^logout/', logout, name='logout'),
]
