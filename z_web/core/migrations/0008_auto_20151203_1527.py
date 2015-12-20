# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20151203_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='obras',
            name='codigo',
            field=models.CharField(db_column='CODIGO', unique=True, max_length=255, default='Sin codigo 2015-12-03 18:27:40.345054+00:00'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='obras',
            name='descuenta_francos',
            field=models.BooleanField(verbose_name='Se utiliza para francos', db_column='DESCUENTA_FRANCOS', default=False),
        ),
        migrations.AlterField(
            model_name='obras',
            name='descuenta_licencias',
            field=models.BooleanField(verbose_name='Se utiliza para licencias anuales', db_column='DESCUENTA_LICENCIAS', default=False),
        ),
        migrations.AlterField(
            model_name='obras',
            name='es_cc',
            field=models.BooleanField(verbose_name='Tratar como CC', help_text='Si está seleccionada, la obra es considerada un CC y se utiliza para los cálculos de costos', default=False),
        ),
        migrations.AlterField(
            model_name='obras',
            name='prorratea_combustible',
            field=models.BooleanField(verbose_name='¿Prorratea Combustible?', help_text='Si está seleccionada, los costos de combustibles se prorratean en los demás CC', default=False),
        ),
        migrations.AlterField(
            model_name='obras',
            name='prorratea_manoobra',
            field=models.BooleanField(verbose_name='¿Prorratea Mano de Obra?', help_text='Si está seleccionada, los costos de mano de obra se prorratean en los demás CC', default=False),
        ),
        migrations.AlterField(
            model_name='obras',
            name='prorratea_materiales',
            field=models.BooleanField(verbose_name='¿Prorratea Materiales?', help_text='Si está seleccionada, los costos de materiales se prorratean en los demás CC', default=False),
        ),
    ]
