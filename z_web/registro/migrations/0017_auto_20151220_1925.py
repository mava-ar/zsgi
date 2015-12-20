# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0016_auto_20151220_1924'),
    ]

    operations = [
        migrations.RunSQL(
            "update registro_equipo as re left join materiales m on m.ID_REGISTROEQUIPO = re.ID "
            "set re.cantera_cargadero = m.CANTERA_CARGADERO, re.cantidad = m.CANTIDAD, "
            "re.viajes = m.VIAJES, re.distancia = m.DISTANCIA, re.material = m.MATERIAL where 1;"
        )
    ]
