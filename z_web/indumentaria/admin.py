from django.contrib import admin

from .models import Epp, EppEntrega, EppEntregaItem, EppOperarios


@admin.register(Epp)
class EppAdmin(admin.ModelAdmin):
    pass


@admin.register(EppEntrega)
class EppEntregaAdmin(admin.ModelAdmin):
    pass


@admin.register(EppEntregaItem)
class EppEntregaItemAdmin(admin.ModelAdmin):
    pass


@admin.register(EppOperarios)
class EppOperariosAdmin(admin.ModelAdmin):
    pass
