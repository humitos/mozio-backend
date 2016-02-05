# from django.contrib import admin
from django.contrib.gis import admin
from serviceareas.models import Provider, ServiceArea


admin.site.register(Provider)
admin.site.register(ServiceArea, admin.OSMGeoAdmin)
