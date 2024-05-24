from django.urls import path

from example import views
from service_orders.views import (
    ServiceOrdersListView,
    ServiceOrdersCreateView,
    ServiceOrdersUpdateView,
    ServiceOrdersDeleteView,
    ServiceOrdersReadView,
    ServiceOrdersFinishView
)

urlpatterns = [
    path("list", ServiceOrdersListView.as_view(), name="service_orders_list"),
    path("create", ServiceOrdersCreateView.as_view(), name="service_orders_create"),
    path("update/<int:pk>", ServiceOrdersUpdateView.as_view(), name="service_orders_update"),
    path("delete/<int:pk>", ServiceOrdersDeleteView.as_view(), name="service_orders_delete"),
    path("read/<int:pk>", ServiceOrdersReadView.as_view(), name="service_orders_read"),
    path("finish/<int:pk>", ServiceOrdersFinishView.as_view(), name="service_orders_finish"),
]
