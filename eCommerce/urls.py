"""eCommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from shop_auth_app import urls as auth_urls
from shop_auth_app.forms import CustomRegistrationForm

from registration.backends.simple import urls as reg_urls
from registration.backends.simple.views import RegistrationView


from shop_app.views import (
    index, no_page, checkout, wishlist, contact,
    product, product_detail, account,
    get_cart, add_to_cart, remove_from_cart  # subscribe
)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'),
    url(r'^error/', no_page, name='no_page'),
    url(r'^(?P<product_id>\d+)/(?P<quantity>\d+)$', add_to_cart, name='add_to_cart'),
    url(r'^(?P<product_id>\d+)$', remove_from_cart, name='remove_from_cart'),
    url(r'^cart/', get_cart, name='cart'),
    url(r'^checkout/', checkout, name='checkout'),
    url(r'^wishlist/', wishlist, name='wishlist'),
    url(r'^contact/', contact, name='contact'),
    url(r'^product/', product, name='product'),
    url(r'^product-detail/(?P<product_id>\d+)$', product_detail, name='product_detail_id'),
    url(r'^product-detail/', product_detail, name='product_detail'),
    url(r'^account/', account, name='account'),
    url(r'^product-detail/(?P<product_id>\d+)$', product_detail, name='product_detail_id'),
    # url(r'^subscribe/', subscribe, name='subscribe'),

    url(r'^register/$',
        RegistrationView.as_view(
            form_class=CustomRegistrationForm, template_name='shop_auth_app/register.html'
        ),
        name='registration_register',
        ),

    url(r'^', include(auth_urls, namespace='shop_auth_app')),
    url(r'^', include(reg_urls, namespace='shop_auth_app')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()


