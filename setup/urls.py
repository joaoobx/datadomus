from django.contrib import admin
from django.urls import path

from example import views
from example.views import (
    ExampleListView,
    ExampleCreateView,
    ExampleUpdateView,
    ExampleDeleteView,
    ExampleCompleteView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", ExampleListView.as_view(), name="example_list"),
    path("get-all", views.listAll, name="example_list_all"),
    path("create", ExampleCreateView.as_view(), name="example_create"),
    path("update/<int:pk>", ExampleUpdateView.as_view(), name="example_update"),
    path("delete/<int:pk>", ExampleDeleteView.as_view(), name="example_delete"),
    path("complete/<int:pk>", ExampleCompleteView.as_view(), name="example_complete"),
]
