from django.contrib import admin

from .models import Patient, SideEffectsRisks


class PatientAdmin(admin.ModelAdmin):
    list_display = ("name", "age")


class SideEffectsRisksAdmin(admin.ModelAdmin):
    list_display = ("patient", "category", "description")


admin.site.register(Patient, PatientAdmin)
admin.site.register(SideEffectsRisks, SideEffectsRisksAdmin)