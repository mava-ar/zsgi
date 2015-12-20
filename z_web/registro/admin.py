from datetime import datetime
from django.contrib import admin

from .models import (Alarma, Combustible, Partediario, Registro,
                     RegistroEquipo, Materiales, PrecioHistorico, Certificacion)
from zweb_utils.format import currency_format as cur


@admin.register(Alarma)
class AlarmaAdmin(admin.ModelAdmin):
    model = Alarma
    list_display = ['alert_status', 'fecha', 'nombre', 'comentario', ]
    order_by = ['-fecha', ]

    def alert_status(self, obj):
        now = datetime.now().date()
        diff = (obj.fecha - now).days
        if diff >= 20:
            return '<i class="icon-time label-success"></i> En %s días' % diff
        elif diff < 20 and diff >= 0:
            return '<i class="icon-time label-warning"></i> En %s' % diff
        else:
            return '<i class="icon-time label-danger"></i> Pasada en %s días' % (diff*-1)
    alert_status.short_description = "Estado"
    alert_status.allow_tags = True


class RegistroAdminInline(admin.TabularInline):
    model = Registro
    extra = 0
    max_num = 1


class RegistroEquipoAdminInline(admin.TabularInline):
    model = RegistroEquipo
    extra = 0
    max_num = 1
    raw_id_fields = ("equipo", )


@admin.register(Partediario)
class PartediarioAdmin(admin.ModelAdmin):
    model = Partediario
    list_display = ('fecha', 'numero', 'operario', 'obra', 'multifuncion', 'desarraigo',)
    order_by = ('-fecha', )
    list_select_related = ('operario', 'obra', 'equipo', )
    search_fields = ['numero', '^operario__nombre', 'fecha']
    list_filter = ('obra', 'multifuncion', 'desarraigo', )
    #inlines = [RegistroEquipoAdminInline, RegistroAdminInline, ]


@admin.register(Registro)
class RegistroAdmin(admin.ModelAdmin):
    pass


@admin.register(RegistroEquipo)
class RegistroEquipoAdmin(admin.ModelAdmin):
    pass


@admin.register(Materiales)
class MaterialesAdmin(admin.ModelAdmin):
    pass


@admin.register(Combustible)
class CombustibleAdmin(admin.ModelAdmin):
    pass


@admin.register(PrecioHistorico)
class PrecioHistoricoAdmin(admin.ModelAdmin):
    list_display = ('familia', 'tipo', 'valor_format', 'fechaalta', 'fechabaja')
    list_filter = ('familia', 'tipo', )

    def valor_format(self, obj):
        return cur(obj.valor)
    valor_format.short_description = "Valor ($)"


@admin.register(Certificacion)
class CertificacionAdmin(admin.ModelAdmin):
    list_display = ('periodo', 'obra', 'valor_format')
    list_filter = ('periodo', 'obra', )

    def valor_format(self, obj):
        return cur(obj.monto)
    valor_format.short_description = "Monto ($)"