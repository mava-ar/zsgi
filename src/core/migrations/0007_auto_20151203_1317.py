# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20151126_2055'),
    ]

    operations = [
        migrations.AddField(
            model_name='obras',
            name='es_cc',
            field=models.BooleanField(verbose_name='Tratar como CC', default=False),
        ),
        migrations.AddField(
            model_name='obras',
            name='prorratea_combustible',
            field=models.BooleanField(verbose_name='¿Prorratea Combustible?', default=False),
        ),
        migrations.AddField(
            model_name='obras',
            name='prorratea_manoobra',
            field=models.BooleanField(verbose_name='¿Prorratea Mano de Obra?', default=False),
        ),
        migrations.AddField(
            model_name='obras',
            name='prorratea_materiales',
            field=models.BooleanField(verbose_name='¿Prorratea Materiales?', default=False),
        ),
    ]
