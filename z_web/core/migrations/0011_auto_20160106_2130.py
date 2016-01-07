# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20160106_2124'),
    ]

    operations = [
        migrations.AddField(
            model_name='obras',
            name='fecha_fin',
            field=models.DateField(help_text='Si está establecido, esta obra o CC no será mostrado en listas desplegables (se considera inactiva).', null=True, blank=True, verbose_name='Fecha de finalización'),
        ),
        migrations.AddField(
            model_name='obras',
            name='incluir_en_costos',
            field=models.BooleanField(help_text='Si está seleccionado, el CC será utilizado en el cálculos de costos.', verbose_name='Incluir en cálculos de costos', default=False),
        ),
        migrations.AlterField(
            model_name='obras',
            name='es_cc',
            field=models.BooleanField(help_text='Si está seleccionada, la obra es considerada un Centro de Costos (CC)', verbose_name='Tratar como CC', default=False),
        ),
    ]
