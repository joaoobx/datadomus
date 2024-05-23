from django.urls import path

from convocations.views import (
    ConvocationsListView,
    ConvocationsCreateView,
    ConvocationsUpdateView,
    ConvocationsDeleteView
)

urlpatterns = [
    path("list", ConvocationsListView.as_view(), name="convocations_list"),
    path("create", ConvocationsCreateView.as_view(), name="convocations_create"),
    path("update/<int:pk>", ConvocationsUpdateView.as_view(), name="convocations_update"),
    path("delete/<int:pk>", ConvocationsDeleteView.as_view(), name="convocations_delete"),
]
