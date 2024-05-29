from django.contrib import admin

from .models import Owner, Vehicle

class OwnerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone')
    search_fields = ('first_name', 'last_name', 'email', 'phone')
    
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('plate_number', 'model', 'owner')
    search_fields = ('plate_number', 'model', 'owner')
    
admin.site.register(Owner, OwnerAdmin)
admin.site.register(Vehicle, VehicleAdmin)