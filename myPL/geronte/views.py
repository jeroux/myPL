from typing import Any

from django.views.generic import FormView
from django.views.generic.edit import DeleteView

from .models import Patient, SideEffectsRisks, CATEGORY_SIDE_EFFECTS
from .forms import SideEffectsForm

class DashboardView(FormView):
    template_name = "geronte/dashboard.html"
    form_class = SideEffectsForm
    success_url = "/"

    def form_valid(self, form: SideEffectsForm):
        patient = Patient.objects.first()
        SideEffectsRisks.objects.create(
            patient=patient,
            category=form.cleaned_data["category"],
            description=form.cleaned_data["description"],
        )
        return super(DashboardView, self).form_valid(form)

    def get_context_data(self, **kwargs: Any):
        context = super(DashboardView, self).get_context_data(**kwargs)
        patient = Patient.objects.first()
        context["object_list"] = SideEffectsRisks.objects.filter(patient=patient).order_by("-id")
        context["side_effects_categories"] = CATEGORY_SIDE_EFFECTS
        return context

class DeleteSideEffectView(DeleteView):
    model = SideEffectsRisks
    success_url = "/"

    


    
    

