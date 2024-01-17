from django.urls import path

from . import views

urlpatterns = [
    path("", views.DashboardView.as_view(), name="dashboard"),
    path("delete_side_effect/<int:pk>/", views.DeleteSideEffectView.as_view(), name="delete_side_effect"),
]
