from django.conf.urls import url

from frontend import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^exportar_xls/$', views.export_panel_control_excel, name='export_panel_control_excel'),
]
