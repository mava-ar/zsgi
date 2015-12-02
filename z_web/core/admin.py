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
    pass


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
