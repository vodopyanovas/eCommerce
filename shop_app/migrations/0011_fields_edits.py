# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-01 09:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0010_new_fields'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='image_added',
            new_name='image_add_date',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='path',
            new_name='large',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product_added',
            new_name='product_add_date',
        ),
        migrations.AddField(
            model_name='image',
            name='medium',
            field=models.ImageField(blank=True, upload_to='media/products/'),
        ),
        migrations.AddField(
            model_name='image',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to='media/products/'),
        ),
    ]
