# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-24 17:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_periodo_activo'),
    ]

    operations = [
        migrations.AddField(
            model_name='encuesta',
            name='periodos',
            field=models.ManyToManyField(related_name='encuestas', to='core.Periodo'),
        ),
    ]
