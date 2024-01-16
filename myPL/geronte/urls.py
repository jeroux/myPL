from django.urls import path

from . import views

urlpatterns = [
    path("", views.DashboardView.as_view(), name="dashboard"),
    path("add_side_effects", views.AddSideEffectsView.as_view(), name="add_side_effects"),
    path("save_new_side_effect", views.saveNewSideEffectView, name="save_new_side_effect")
]
