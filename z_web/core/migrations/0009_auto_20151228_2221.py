# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20151203_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='fechabaja',
            field=models.DateTimeField(verbose_name='Fecha de baja', help_text='Si la fecha de baja no está establecida, el usuario está activo.', null=True, db_column='FECHABAJA', blank=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='rol',
            field=models.CharField(max_length=128, db_column='ROL', choices=[('De carga', 'De carga'), ('Administrador', 'Administrador')]),
        ),
    ]
