from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from .models import Parking


# для настройки загрузки сторонней базы через административную панель
class ParkingResource(resources.ModelResource):

    class Meta:
        model = Parking


class ParkingAdmin(ImportExportModelAdmin):
    resource_classes = [ParkingResource]

admin.site.register(Parking, ParkingAdmin)
