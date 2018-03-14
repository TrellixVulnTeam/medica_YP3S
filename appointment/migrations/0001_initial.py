# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-14 15:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(default=None, max_length=64)),
                ('phone_number', models.CharField(default=None, max_length=90)),
                ('email', models.EmailField(blank=True, default=None, max_length=64)),
                ('comment', models.TextField(blank=True, default=None)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Запись на прием',
                'verbose_name_plural': 'Записи на прием',
            },
        ),
    ]
