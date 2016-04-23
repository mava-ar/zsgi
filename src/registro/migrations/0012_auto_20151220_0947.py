# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0011_auto_20151220_0944'),
    ]

    operations = [
        migrations.RunSQL(
                "update registro r inner JOIN partediario p on p.horario = r.id set r.partediario_id = p.id where 1;"
                "update registro_equipo re inner JOIN partediario p on p.EQUIPO = re.ID set re.partediario_id = p.id where 1;"
        )
    ]
