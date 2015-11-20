from django.contrib import admin

from .models import Situacion, Parametro, Funcion


@admin.register(Situacion)
class SituacionAdmin(admin.ModelAdmin):
    pass


@admin.register(Parametro)
class ParametroAdmin(admin.ModelAdmin):
    pass


@admin.register(Funcion)
class FuncionAdmin(admin.ModelAdmin):
    pass


