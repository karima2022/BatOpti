from django.contrib import admin
from .models import Building

@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'building_type')  # Colonnes affichées dans l'admin
