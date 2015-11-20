from datetime import datetime
from django.contrib import admin

from .models import Alarma  #, Partediario, Registro, RegistroEquipo, Materiales, Combustible


@admin.register(Alarma)
class AlarmaAdmin(admin.ModelAdmin):
    model = Alarma
    list_display = ['alert_status', 'fecha', 'nombre', 'comentario', ]
    order_by = ['-fecha', ]

    def alert_status(self, obj):
        now = datetime.now().date()
        diff = (obj.fecha - now).days
        if diff >= 20:
            return '<i class="icon-time label-success"></i> %s' % diff
        elif diff < 20 and diff > 0:
            return '<i class="icon-time label-warning"></i> %s' % diff
        else:
            return '<i class="icon-time label-danger"></i> %s' % diff
    alert_status.short_description = "Estado"
    alert_status.allow_tags = True


# @admin.register(Partediario)
# class PartediarioAdmin(admin.ModelAdmin):
    # pass


# @admin.register(Registro)
# class RegistroAdmin(admin.ModelAdmin):
    # pass


# @admin.register(RegistroEquipo)
# class RegistroEquipoAdmin(admin.ModelAdmin):
    # pass


# @admin.register(Materiales)
# class MaterialesAdmin(admin.ModelAdmin):
    # pass


# @admin.register(Combustible)
# class CombustibleAdmin(admin.ModelAdmin):
    # pass
