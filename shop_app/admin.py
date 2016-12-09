from django.contrib import admin
from shop_app.models import (
    Product, Brand, Category, Options, ProductOptions, OptionsGroups, Image, Country, Subscriber, UserInfo, Address,
)


# Register your models here.
def discount_on(model_admin, request, queryset):
    queryset.update(discount_available="True")
discount_on.short_description = 'Start discount'


def discount_off(model_admin, request, queryset):
    queryset.update(discount_available="False")
discount_off.short_description = 'Off discount'


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'gender',
        'brand',
        'category',
        'product_name',
        'unit_price',
        'discount',
        # 'product_weight',
        'product_stock',
        'products_ordered',
        # 'products_available',
        'discount_available',
        'is_bestseller',
        'made_in',
    )

    list_editable = (
        'unit_price',
        'discount',
        'product_stock',
    )

    list_filter = ('category__category_name', 'brand__brand_name',)

    search_fields = (
        'sku',
        'product_name',
        'brand__brand_name',
        'category__category_name',
    )

    actions = (
        discount_on,
        discount_off,
    )
admin.site.register(Product, ProductAdmin)


class BrandAdmin(admin.ModelAdmin):
    list_display = (
        'brand_name',
    )
admin.site.register(Brand, BrandAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'category_name',
    )
admin.site.register(Category, CategoryAdmin)


class OptionAdmin(admin.ModelAdmin):
    list_display = (
        'option_group',
        'option_name',
    )

    list_editable = (
        'option_name',
    )

    list_filter = ('option_group__option_group_name',)
admin.site.register(Options, OptionAdmin)


class ProductOptionAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'option_group',
        'option',
    )

    list_filter = ('option_group__option_group_name','product__product_name')
    search_fields = ('product__product_name',)
admin.site.register(ProductOptions, ProductOptionAdmin)


class OptionsGroupAdmin(admin.ModelAdmin):
    list_display = (
        'option_group_name',
    )
admin.site.register(OptionsGroups, OptionsGroupAdmin)


class ImageUploadAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'alt',
    )

    search_fields = (
        'product__product_name',
    )
admin.site.register(Image, ImageUploadAdmin)


class SubscriberAdmin(admin.ModelAdmin):
    list_display = (
        'email',
    )

    search_fields = (
        'email',
    )
admin.site.register(Subscriber, SubscriberAdmin)


class CountryAddAdmin(admin.ModelAdmin):
    list_display = (
        'country_name',
    )
admin.site.register(Country, CountryAddAdmin)


class UserInfoAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'name',
        'last_name',
        'company_name',
        'phone',
    )

    list_filter = (
        'user__email',
    )
admin.site.register(UserInfo, UserInfoAdmin)


class AddressAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'country',
        'city',
        'address',
        'apartment',
        'district',
        'postcode',
    )

    list_filter = (
        'country',
    )
admin.site.register(Address, AddressAdmin)
