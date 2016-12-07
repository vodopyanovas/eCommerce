# # -*- coding: utf-8 -*-
#
# __author__ = 'Anton Vodopyanov'
#
# from django.conf.urls import url
#
# from django.contrib.auth.views import login, logout_then_login
# from django.views.generic import CreateView
#
# # from shop_auth_app.forms import CustomCreationForm
#
#
# urlpatterns = [
#     url(r'^login/', login, {
#         'template_name': 'auth_app/login.html',
#     }, name='login'),
#     url(r'^logout/', logout_then_login, name='logout'),
#
#     url(r'^register/', CreateView.as_view(
#         # template_name='auth_app/register.html',
#         template_name='shop_auth_app/account.html',
#         form_class=CustomCreationForm,
#         success_url='/'
#     ), name='register'),
# ]