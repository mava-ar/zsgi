from django import forms
from functools import partial, wraps
from django.forms.models import ModelForm, BaseInlineFormSet
from django.forms.formsets import BaseFormSet, formset_factory


from .models import CostoSubContrato
from core.models import Obras
from parametros.models import Periodo, FamiliaEquipo


class PeriodoSelectForm(forms.Form):
    periodo = forms.ModelChoiceField(queryset=Periodo.objects.all())


# class TipoCostoObraForm(forms.Form):
#     TIPO_COSTO = (
#         ('costomanoobra', 'Costos Mano de Obra'),
#         ('costosubcontrato', 'Costos Subcontratos'),
#         ('lubricantefluidoidro', 'Costos de Lubricantes y Fluidos Hidraulicos'),
#         ('trenrodaje', 'Costos de Tren de Rodaje'),
#         ('reservereparaciones', 'Reserva de reparaciones'),
#         ('costoposesion', 'Costos de posesión'),
#         ('materialestotal', 'Costos de Materiales'),
#         ('servicioprestadoun', 'Servicio Prestados en otras UN'),
#     )
#     tipo_costos = forms.ChoiceField(choices=TIPO_COSTO, widget=forms.RadioSelect())


class CostoItemForm(forms.Form):
    monto = forms.FloatField(required=False)
    obra = forms.ModelChoiceField(Obras.objects.filter(es_cc=True), widget=forms.HiddenInput())


class CostoItemFamiliaForm(forms.Form):
    monto = forms.FloatField(required=False)
    familia = forms.ModelChoiceField(FamiliaEquipo.objects.all(), widget=forms.HiddenInput())

