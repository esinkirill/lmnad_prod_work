# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2018-04-16 10:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified', models.DateTimeField(auto_now=True, null=True)),
                ('src', models.FileField(upload_to='uploads/tank/data', verbose_name='\u0414\u0430\u043d\u043d\u044b\u0435')),
            ],
            options={
                'verbose_name': '\u0414\u0430\u043d\u043d\u044b\u0435',
                'verbose_name_plural': '\u0414\u0430\u043d\u043d\u044b\u0435',
            },
        ),
        migrations.CreateModel(
            name='Experiment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=255, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('description', models.TextField(blank=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435')),
            ],
            options={
                'verbose_name': '\u042d\u043a\u0441\u043f\u0435\u0440\u0438\u043c\u0435\u043d\u0442',
                'verbose_name_plural': '\u042d\u043a\u0441\u043f\u0435\u0440\u0438\u043c\u0435\u043d\u0442\u044b',
            },
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified', models.DateTimeField(auto_now=True, null=True)),
                ('src', models.ImageField(max_length=255, upload_to='uploads/tank/images', verbose_name='\u0424\u043e\u0442\u043e')),
                ('experiment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='tank.Experiment', verbose_name='\u042d\u043a\u0441\u043f\u0435\u0440\u0438\u043c\u0435\u043d\u0442')),
            ],
            options={
                'verbose_name': '\u0424\u043e\u0442\u043e',
                'verbose_name_plural': '\u0424\u043e\u0442\u043e',
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified', models.DateTimeField(auto_now=True, null=True)),
                ('src', models.FileField(help_text='\u0412\u0438\u0434\u0435\u043e, \u0433\u0438\u0444\u043a\u0430', upload_to='uploads/tank/movies', verbose_name='\u0417\u0430\u043f\u0438\u0441\u044c')),
                ('experiment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movies', to='tank.Experiment', verbose_name='\u042d\u043a\u0441\u043f\u0435\u0440\u0438\u043c\u0435\u043d\u0442')),
            ],
            options={
                'verbose_name': '\u0412\u0438\u0434\u0435\u043e',
                'verbose_name_plural': '\u0412\u0438\u0434\u0435\u043e',
            },
        ),
        migrations.AddField(
            model_name='data',
            name='experiment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='data', to='tank.Experiment', verbose_name='\u042d\u043a\u0441\u043f\u0435\u0440\u0438\u043c\u0435\u043d\u0442'),
        ),
    ]
