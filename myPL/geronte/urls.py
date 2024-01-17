from django.urls import path

from . import views

urlpatterns = [
    path("", views.DashboardView.as_view(), name="dashboard"),
    path("delete_side_effect/<int:pk>/", views.deleteSideEffect, name="delete_side_effect"),
    path("update_side_effect", views.updateSideEffect, name="update_side_effect"),
]
