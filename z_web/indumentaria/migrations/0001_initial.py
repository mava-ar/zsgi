# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20151026_0017'),
    ]

    operations = [
        migrations.CreateModel(
            name='Epp',
            fields=[
                ('id', models.AutoField(primary_key=True, db_column='ID', serialize=False)),
                ('nombre', models.CharField(db_column='NOMBRE', max_length=45)),
                ('medida', models.CharField(db_column='MEDIDA', max_length=45)),
            ],
            options={
                'verbose_name_plural': 'indumentaria',
                'verbose_name': 'indumentaria',
                'db_table': 'epp',
            },
        ),
        migrations.CreateModel(
            name='EppEntrega',
            fields=[
                ('id', models.AutoField(primary_key=True, db_column='ID', serialize=False)),
                ('fecha', models.DateField(db_column='FECHA')),
                ('observaciones', models.TextField(null=True, db_column='OBSERVACIONES', blank=True)),
                ('operario', models.ForeignKey(to='core.Operarios', db_column='operarioId')),
            ],
            options={
                'verbose_name_plural': 'entregas de indumentaria',
                'verbose_name': 'entrega de indumentaria',
                'db_table': 'epp_entrega',
            },
        ),
        migrations.CreateModel(
            name='EppEntregaItem',
            fields=[
                ('id', models.AutoField(primary_key=True, db_column='ID', serialize=False)),
                ('medida', models.CharField(db_column='MEDIDA', max_length=45)),
                ('epp', models.ForeignKey(to='indumentaria.Epp', null=True, blank=True)),
                ('epp_entrega', models.ForeignKey(to='indumentaria.EppEntrega', db_column='EPP_ENTREGA_ID')),
            ],
            options={
                'verbose_name_plural': 'ítems entregas de indumentaria',
                'verbose_name': 'ítem de entrega de indumentaria',
                'db_table': 'epp_entrega_item',
            },
        ),
        migrations.CreateModel(
            name='EppOperarios',
            fields=[
                ('id', models.AutoField(primary_key=True, db_column='ID', serialize=False)),
                ('valor', models.CharField(null=True, db_column='VALOR', max_length=128, blank=True)),
                ('tipo', models.IntegerField(db_column='TIPO')),
                ('epp', models.ForeignKey(to='indumentaria.Epp', db_column='EPP_ID')),
                ('operario', models.ForeignKey(to='core.Operarios', db_column='OPERARIO_ID')),
            ],
            options={
                'verbose_name_plural': 'datos de indumentaria de operarios',
                'verbose_name': 'dato de indumentario de operario',
                'db_table': 'epp_operarios',
            },
        ),
    ]
