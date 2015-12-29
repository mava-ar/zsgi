# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0010_certificacion'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='certificacion',
            options={'verbose_name_plural': 'certificaciones', 'verbose_name': 'certificación'},
        ),
        migrations.AddField(
            model_name='registro',
            name='partediario',
            field=models.OneToOneField(null=True, to='registro.Partediario', blank=True, verbose_name='Parte Diario'),
        ),
        migrations.AddField(
            model_name='registroequipo',
            name='partediario',
            field=models.OneToOneField(null=True, to='registro.Partediario', blank=True, verbose_name='Parte Diario'),
        ),
        migrations.AlterField(
            model_name='partediario',
            name='equipo',
            field=models.ForeignKey(null=True, to='registro.RegistroEquipo', related_name='parte_diario_registro_equipo', db_column='EQUIPO', blank=True),
        ),
        migrations.AlterField(
            model_name='partediario',
            name='horario',
            field=models.OneToOneField(null=True, to='registro.Registro', related_name='parte_diario_horario', db_column='HORARIO', blank=True),
        ),
        migrations.AlterUniqueTogether(
            name='certificacion',
            unique_together=set([('periodo', 'obra')]),
        ),
    ]
