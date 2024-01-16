from django import forms
from django.utils.translation import gettext_lazy as _

from .models import SideEffectsRisks

class SideEffectsForm(forms.ModelForm):
    class Meta:
        model = SideEffectsRisks
        fields = ("category", "description")

        widgets = {
            "category": forms.HiddenInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
        }