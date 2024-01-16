from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from .models import SideEffectsRisks, CATEGORY_SIDE_EFFECTS

class DashboardView(ListView):
    template_name = "geronte/dashboard.html"
    model = SideEffectsRisks
    paginate_by = 100

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["side_effects_categories"] = CATEGORY_SIDE_EFFECTS
        return context

class AddSideEffectsView(TemplateView):
    template_name = "geronte/partials/side_effects_partial.html"
    

