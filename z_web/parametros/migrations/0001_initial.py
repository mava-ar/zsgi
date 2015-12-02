# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FamiliaEquipo',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('nombre', models.CharField(blank=True, null=True, max_length=255)),
            ],
            options={
                'db_table': 'familia_equipo',
            },
        ),
        migrations.CreateModel(
            name='Funcion',
            fields=[
                ('id', models.AutoField(db_column='ID', serialize=False, primary_key=True)),
                ('funcion', models.CharField(db_column='FUNCION', unique=True, max_length=128)),
            ],
            options={
                'db_table': 'funcion',
            },
        ),
        migrations.CreateModel(
            name='Parametro',
            fields=[
                ('clave', models.CharField(db_column='CLAVE', primary_key=True, serialize=False, max_length=45)),
                ('clave_grupo', models.CharField(db_column='CLAVE_GRUPO', blank=True, null=True, max_length=45)),
                ('valor', models.CharField(db_column='VALOR', blank=True, null=True, max_length=128)),
            ],
            options={
                'db_table': 'parametro',
            },
        ),
        migrations.CreateModel(
            name='Situacion',
            fields=[
                ('id', models.AutoField(db_column='ID', serialize=False, primary_key=True)),
                ('situacion', models.CharField(db_column='SITUACION', max_length=128)),
            ],
            options={
                'db_table': 'situacion',
            },
        ),
        migrations.CreateModel(
            name='TipoCosto',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('nombre', models.CharField(blank=True, null=True, max_length=255)),
                ('tipo', models.IntegerField(unique=True)),
            ],
            options={
                'db_table': 'tipo_costo',
            },
        ),
    ]
