from django.contrib import admin
from django.conf.urls import patterns
from django.http import HttpResponse
from django.contrib.admin.sites import AdminSite



# class EstadisticaAdmin(AdminSite):
#
#     def get_urls(self):
#         urls = super(EstadisticaAdmin, self).get_urls()
#         my_urls = patterns(
#             '',
#             (r'^estadistica/$', EstadisticaView.as_view()),
#         )
#         return my_urls + urls


