from django.contrib import admin
from .models import tbl_district, tbl_place, tbl_stationmaster, tbl_eventtype, tbl_boat, tbl_canteen
# Register your models here.
admin.site.register(tbl_district)
admin.site.register(tbl_place)
admin.site.register(tbl_stationmaster)
admin.site.register(tbl_eventtype)
admin.site.register(tbl_boat)
admin.site.register(tbl_canteen)
