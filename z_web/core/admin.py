from django.contrib import admin

from core.models import (Equipos, EstServicio, FrancoLicencia, Obras,
                         Operarios, Usuario)


@admin.register(Equipos)
class Equipos(admin.ModelAdmin):
    pass


@admin.register(EstServicio)
class EstacionServicioAdmin(admin.ModelAdmin):
    pass


@admin.register(Obras)
class ObrasAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'obra', 'cuit', 'lugar', 'responsable', )
    list_filter = ('responsable', 'descuenta_francos', 'descuenta_licencias', "es_cc", )
    search_fields = ('codigo', 'obra', 'comitente', 'responsable', 'cuit', )

    fieldsets = (
        (None, {
            'fields': (('codigo', 'obra', 'fecha_inicio'),
                       ('cuit', 'lugar', 'plazo'),
                       ('contrato', 'comitente', 'responsable',))
        }),
        ("Configuración General", {
            'fields': ('tiene_registro', 'tiene_equipo', 'descuenta_francos', 'descuenta_licencias', )
        }),
        ("Configuración de registro horario", {
            'fields': ('tiene_comida', 'tiene_vianda', 'tiene_desarraigo', 'limite_vianda_doble', )
        }),
        ("Configuración de costos", {
            'fields': ('es_cc', 'prorratea_combustible', 'prorratea_manoobra', 'prorratea_materiales', )
        })
    )


class FrancoLicenciaInlineAdmin(admin.StackedInline):
    extra = 0
    can_delete = False
    model = FrancoLicencia
    max_num = 1
    fieldsets = (
        ("Parámetros de ajustes", {
            'fields': (('ajuste_francos', 'ajuste_licencias', 'pagados',),)
        }),
        ("Solicitud de días", {
            'fields': (('solicitados1', 'sale1', 'entra1', ),
                       ('solicitados2', 'sale2', 'entra2', )),
        }),
    )


@admin.register(Operarios)
class OperariosAdmin(admin.ModelAdmin):
    list_display = ('n_legajo', 'nombre', 'cuil', 'funcion', 'desarraigo',
                    'fecha_ingreso', 'observaciones')
    list_filter = ('funcion', 'desarraigo', )
    search_fields = ('^n_legajo', '^cuil', 'nombre', '^fecha_ingreso', )
    list_display_links = ('n_legajo', 'nombre', )
    fieldsets = (
        (None, {
            'fields': (('n_legajo', 'cuil', ),
                       ('nombre', ))
        }),

        ('Funciones', {
            'fields': (('funcion', 'desarraigo',), )
        }),
        ('Fechas Importantes', {
            'fields': ('fecha_ingreso',
                       ('vto_carnet', 'vto_psicofisico'),
                       ('vto_cargagral', 'vto_cargapeligrosa'), )
        }),
        ('Vencimientos extras', {
            'classes': ('collapse',),
            'fields': (('descripcion_vto1', 'vto_otros1', ),
                       ('descripcion_vto2', 'vto_otros2', ),
                       ('descripcion_vto3', 'vto_otros3', ),)
        }),
        ("Observaciones", {
            'classes': ('collapse',),
            'fields': ('observaciones', )
        }),
    )
    inlines = [FrancoLicenciaInlineAdmin, ]


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    pass
