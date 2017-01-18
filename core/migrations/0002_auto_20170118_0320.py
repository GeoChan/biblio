# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-18 08:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Busqueda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libro', models.CharField(max_length=8)),
                ('nombre', models.CharField(max_length=128)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Libro')),
                ('periodo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Periodo')),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Persona')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='registro',
            unique_together=set([('pregunta', 'codigo', 'periodo')]),
        ),
        migrations.AddField(
            model_name='busqueda',
            name='libro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Libro'),
        ),
        migrations.AddField(
            model_name='busqueda',
            name='periodo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Periodo'),
        ),
    ]
