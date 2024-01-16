from typing import Any

from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, FormView
from django.http import HttpResponse

from .models import SideEffectsRisks, CATEGORY_SIDE_EFFECTS
from .forms import SideEffectsForm

class DashboardView(ListView):
    template_name = "geronte/dashboard.html"
    model = SideEffectsRisks
    paginate_by = 100

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["side_effects_categories"] = CATEGORY_SIDE_EFFECTS
        return context

class AddSideEffectsView(View):
    """
        View that return a form in a partial.
        Called by HTMX
    """
    def post(self, request: Any) -> Any:
        categories = [category[1] for category in CATEGORY_SIDE_EFFECTS]
        if request.POST.get("category") not in  categories:
           return HttpResponse('')
        
        form = SideEffectsForm(request.POST)
        return render(request, "geronte/partials/side_effects_partial.html", {"category": request.POST.get("category"), "form": form})
    
def saveNewSideEffectView(request):
    if request.method == "POST":
        form = SideEffectsForm(request.POST)
        
        if not form.is_valid():
            return HttpResponse('')
        
        description = request.POST.get("description")
        category = request.POST.get("category")
        SideEffectsRisks.objects.create(description=description, category=category)
        return redirect("dashboard")
    return HttpResponse('')

    


    
    

