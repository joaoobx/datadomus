from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import CarReservations, SpaceReservations


class CarReservationsListView(LoginRequiredMixin, ListView):
    model = CarReservations

class CarReservationsCreateView(LoginRequiredMixin, CreateView):
    model = CarReservations
    fields = ["user", "tenant_name", "apartment"]
    success_url = reverse_lazy("car_reservations_list")

class CarReservationsUpdateView(LoginRequiredMixin, UpdateView):
    model = CarReservations
    fields = ["user", "tenant_name", "apartment"]
    success_url = reverse_lazy("car_reservations_list")

class CarReservationsDeleteView(LoginRequiredMixin, DeleteView):
    model = CarReservations
    success_url = reverse_lazy("car_reservations_list")

class SpaceReservationsListView(LoginRequiredMixin, ListView):
    model = SpaceReservations

class SpaceReservationsCreateView(LoginRequiredMixin, CreateView):
    model = SpaceReservations
    fields = ["user", "description", "apartment"]
    success_url = reverse_lazy("space_reservations_list")

class SpaceReservationsUpdateView(LoginRequiredMixin, UpdateView):
    model = SpaceReservations
    fields = ["user", "description", "apartment"]
    success_url = reverse_lazy("space_reservations_list")

class SpaceReservationsDeleteView(LoginRequiredMixin, DeleteView):
    model = SpaceReservations
    success_url = reverse_lazy("space_reservations_list")
