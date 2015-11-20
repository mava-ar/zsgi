from django.contrib import admin

from core.models import (Equipos, EstServicio, FrancoLicencia, Obras,
                         Operarios, Usuario)


@admin.register(Equipos)
class Equipos(admin.ModelAdmin):
    pass


@admin.register(EstServicio)
class EstacionServicioAdmin(admin.ModelAdmin):
    pass


@admin.register(FrancoLicencia)
class FrancoLicenciaAdmin(admin.ModelAdmin):
    pass


@admin.register(Obras)
class ObrasAdmin(admin.ModelAdmin):
    pass


@admin.register(Operarios)
class OperariosAdmin(admin.ModelAdmin):
    pass


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    pass
