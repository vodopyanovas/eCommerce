# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-21 15:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0005_test'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TestImage',
        ),
        migrations.RenameField(
            model_name='options',
            old_name='option_group_id',
            new_name='option_group',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='category_id',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='SKU',
            new_name='sku',
        ),
        migrations.RenameField(
            model_name='productoptions',
            old_name='option_id',
            new_name='option',
        ),
        migrations.RenameField(
            model_name='productoptions',
            old_name='option_group_id',
            new_name='option_group',
        ),
        migrations.RenameField(
            model_name='productoptions',
            old_name='product_id',
            new_name='product',
        ),
        migrations.RemoveField(
            model_name='product',
            name='vendor_id',
        ),
    ]
