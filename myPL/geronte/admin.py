from django.contrib import admin

from .models import Patient, SideEffectsRisks


class PatientAdmin(admin.ModelAdmin):
    list_display = ("name", "age", "drugs_allergies")


class SideEffectsRisksAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "category")


admin.site.register(Patient, PatientAdmin)
admin.site.register(SideEffectsRisks, SideEffectsRisksAdmin)