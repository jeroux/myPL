from typing import Any

from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.views.generic.edit import DeleteView
from django.http import HttpResponse

from .models import Patient, SideEffectsRisks, CATEGORY_SIDE_EFFECTS
from .forms import SideEffectsForm

class DashboardView(FormView):
    template_name = "geronte/dashboard.html"
    form_class = SideEffectsForm
    success_url = "/"

    def form_valid(self, form: SideEffectsForm) -> HttpResponse:
        patient = Patient.objects.first()
        SideEffectsRisks.objects.create(
            patient=patient,
            category=form.cleaned_data["category"],
            description=form.cleaned_data["description"],
        )
        return super(DashboardView, self).form_valid(form)

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super(DashboardView, self).get_context_data(**kwargs)
        patient = Patient.objects.first()
        context["object_list"] = SideEffectsRisks.objects.filter(patient=patient)
        context["side_effects_categories"] = CATEGORY_SIDE_EFFECTS
        return context

class DeleteSideEffectView(DeleteView):
    model = SideEffectsRisks
    success_url = "/"

    


    
    

