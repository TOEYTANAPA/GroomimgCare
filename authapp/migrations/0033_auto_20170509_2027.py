# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-05-09 13:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0032_auto_20170509_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
