# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20151203_1527'),
        ('parametros', '0004_auto_20151127_1904'),
        ('registro', '0009_auto_20151126_1249'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificacion',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('monto', models.FloatField(verbose_name='Monto ($)')),
                ('obra', models.ForeignKey(to='core.Obras', related_name='certificaciones')),
                ('periodo', models.ForeignKey(to='parametros.Periodo', related_name='certificaciones', verbose_name='Periodo')),
            ],
        ),
    ]
