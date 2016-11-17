# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-17 16:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='is_bestseller',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_description_long',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(blank=True, upload_to=None),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_weight',
            field=models.DecimalField(blank=True, decimal_places=3, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='product',
            name='vendor_id',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]
