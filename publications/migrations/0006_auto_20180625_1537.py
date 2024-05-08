# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2018-06-25 12:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0005_auto_20180621_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authorpublication',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='authors', to='publications.Author', verbose_name='\u0410\u0432\u0442\u043e\u0440'),
        ),
        migrations.AlterField(
            model_name='authorpublication',
            name='publication',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='publications', to='publications.Publication', verbose_name='\u041f\u0443\u0431\u043b\u0438\u043a\u0430\u0446\u0438\u044f'),
        ),
    ]
