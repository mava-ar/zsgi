# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0016_auto_20151230_0957'),
    ]

    operations = [
        migrations.AddField(
            model_name='materiales',
            name='partediario',
            field=models.ForeignKey(verbose_name='Parte Diario', null=True, to='registro.Partediario', related_name='materiales_transportados'),
        ),
    ]
