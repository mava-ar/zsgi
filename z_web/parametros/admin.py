from django.contrib import admin

from .models import Situacion, Parametro, Funcion, FamiliaEquipo, TipoCosto, Periodo


@admin.register(Situacion)
class SituacionAdmin(admin.ModelAdmin):
    pass


@admin.register(Parametro)
class ParametroAdmin(admin.ModelAdmin):
    pass


@admin.register(Funcion)
class FuncionAdmin(admin.ModelAdmin):
    pass

@admin.register(FamiliaEquipo)
class FamiliaEquipoAdmin(admin.ModelAdmin):
    pass


@admin.register(TipoCosto)
class TipoCostoAdmin(admin.ModelAdmin):
    pass


@admin.register(Periodo)
class PeriodoAdmin(admin.ModelAdmin):
    pass