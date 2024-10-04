from django.contrib import admin
from .models import Organization, Department, Division, Sector

# Register your models here.


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Division)
class ODivisionAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Sector)
class SectorAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
