from django.urls import path

from reservations.views import (
    CarReservationsListView,
    CarReservationsCreateView,
    CarReservationsUpdateView,
    CarReservationsDeleteView,
    SpaceReservationsListView,
    SpaceReservationsCreateView,
    SpaceReservationsDeleteView,
    SpaceReservationsUpdateView
)

urlpatterns = [
    path("car-reservation-list", CarReservationsListView.as_view(), name="car_reservations_list"),
    path("car-reservation-create", CarReservationsCreateView.as_view(), name="car_reservations_create"),
    path("car-reservation-update/<int:pk>", CarReservationsUpdateView.as_view(), name="car_reservations_update"),
    path("car-reservation-delete/<int:pk>", CarReservationsDeleteView.as_view(), name="car_reservations_delete"),
    path("space-reservation-list", SpaceReservationsListView.as_view(), name="space_reservations_list"),
    path("space-reservation-create", SpaceReservationsCreateView.as_view(), name="space_reservations_create"),
    path("space-reservation-update/<int:pk>", SpaceReservationsUpdateView.as_view(), name="space_reservations_update"),
    path("space-reservation-delete/<int:pk>", SpaceReservationsDeleteView.as_view(), name="space_reservations_delete"),
]
