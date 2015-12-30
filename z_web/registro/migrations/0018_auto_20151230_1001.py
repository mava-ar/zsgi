# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0017_materiales_partediario'),
    ]

    operations = [
        migrations.RunSQL(
           "update materiales as m left join registro_equipo re on m.ID_REGISTROEQUIPO = re.ID "
           "LEFT JOIN partediario p on p.ID = re.partediario_id set m.partediario_id = p.ID;",
            ""  # no hace nada al revertir
        )
    ]
