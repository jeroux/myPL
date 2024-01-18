from typing import Any
from django.http import HttpResponse

from django.shortcuts import redirect
from django.views.generic import FormView
from django.views.generic.edit import DeleteView, UpdateView

from .models import Patient, SideEffectsRisks, CATEGORY_SIDE_EFFECTS
from .forms import SideEffectsForm


class DashboardView(FormView):
    """
    Display the main page of the application.

    The context contains:
    - `object_list`: The list of side effects for the current patient. The list is ordered by category.
    - `side_effects_categories`: The list of side effects categories. For adding a new side effect.

    Parameters:
    - `form_class`: The form to use to add a new side effect.
    - `template_name`: The template to use to render the page.
    - `success_url`: The URL to redirect to after a successful POST. Here, the main page.

    Returns:
    - `context`: The context to use to render the page.
    """
    template_name = "geronte/dashboard.html"
    form_class = SideEffectsForm
    success_url = "/"

    def form_valid(self, form: SideEffectsForm):
        """
        Called when the form is valid.
        Add a new side effect to the database.
        For now, the patient is the first patient in the database.
        """
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
        context["object_list"] = SideEffectsRisks.objects.filter(patient=patient).order_by("category")
        context["side_effects_categories"] = CATEGORY_SIDE_EFFECTS
        return context


def deleteSideEffect(request, pk):
    """
    Delete a side effect.

    Parameters:
    - `request`: The request object.
    - `pk`: The primary key of the side effect to delete.

    Returns:
    - `redirect`: Redirect to the main page.
    """

    SideEffectsRisks.objects.filter(pk=pk).delete()
    return redirect("/")

def updateSideEffect(request):
    """
    Update a side effect with a new description.

    Parameters:
    - `request`: The request object.

    Returns:
    - `redirect`: Redirect to the main page.
    """
    if request.method == "POST":
        pk = request.POST.get("update")
        SideEffectsRisks.objects.filter(pk=pk).update(description=request.POST.get("description"))
    return redirect("/")

    


    
    

