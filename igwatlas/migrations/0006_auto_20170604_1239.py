# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-06-04 09:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('igwatlas', '0005_auto_20170604_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='path',
            field=models.CharField(blank=True, help_text='uploads/igwatlas/sources/', max_length=500, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0444\u0430\u0439\u043b\u0430, \u043f\u0443\u0442\u044c'),
        ),
    ]