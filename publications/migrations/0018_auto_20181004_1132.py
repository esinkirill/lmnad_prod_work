# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2018-10-04 08:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0017_auto_20181003_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='type',
            field=models.CharField(choices=[('journal', '\u0416\u0443\u0440\u043d\u0430\u043b'), ('conference', '\u041a\u043e\u043d\u0444\u0435\u0440\u0435\u043d\u0446\u0438\u044f')], default='journal', help_text='\u0416\u0443\u0440\u043d\u0430\u043b \u0438\u043b\u0438 \u043a\u043e\u043d\u0444\u0435\u0440\u0435\u043d\u0446\u0438\u044f', max_length=55, verbose_name='\u0422\u0438\u043f'),
        ),
    ]