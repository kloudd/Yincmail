# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-06-10 07:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productId', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('imageUrl', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
                ('weight', models.CharField(max_length=200)),
                ('quantitiy', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.CharField(max_length=200)),
                ('userName', models.CharField(max_length=200)),
                ('userPassword', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('pincode', models.CharField(max_length=200)),
            ],
        ),
    ]
