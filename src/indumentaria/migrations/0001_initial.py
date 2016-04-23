# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Epp',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, db_column='ID')),
                ('nombre', models.CharField(max_length=45, db_column='NOMBRE')),
                ('medida', models.CharField(max_length=45, db_column='MEDIDA')),
            ],
            options={
                'db_table': 'epp',
            },
        ),
        migrations.CreateModel(
            name='EppEntrega',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, db_column='ID')),
                ('fecha', models.DateField(db_column='FECHA')),
                ('observaciones', models.TextField(blank=True, db_column='OBSERVACIONES', null=True)),
                ('operarioid', models.IntegerField(blank=True, db_column='operarioId', null=True)),
            ],
            options={
                'db_table': 'epp_entrega',
            },
        ),
        migrations.CreateModel(
            name='EppEntregaItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, db_column='ID')),
                ('medida', models.CharField(max_length=45, db_column='MEDIDA')),
                ('epp', models.ForeignKey(null=True, blank=True, to='indumentaria.Epp')),
                ('epp_entrega', models.ForeignKey(to='indumentaria.EppEntrega', db_column='EPP_ENTREGA_ID')),
            ],
            options={
                'db_table': 'epp_entrega_item',
            },
        ),
        migrations.CreateModel(
            name='EppOperarios',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, db_column='ID')),
                ('valor', models.CharField(blank=True, max_length=128, db_column='VALOR', null=True)),
                ('tipo', models.IntegerField(db_column='TIPO')),
                ('epp', models.ForeignKey(to='indumentaria.Epp', db_column='EPP_ID')),
                ('operario', models.ForeignKey(to='core.Operarios', db_column='OPERARIO_ID')),
            ],
            options={
                'db_table': 'epp_operarios',
            },
        ),
    ]
