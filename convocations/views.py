from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Convocations


class ConvocationsListView(LoginRequiredMixin, ListView):
    model = Convocations

class ConvocationsCreateView(LoginRequiredMixin, CreateView):
    model = Convocations
    fields = ["title", "description", "doc_url"]
    success_url = reverse_lazy("convocations_list")

class ConvocationsUpdateView(LoginRequiredMixin, UpdateView):
    model = Convocations
    fields = ["title", "description", "doc_url"]
    success_url = reverse_lazy("convocations_list")

class ConvocationsDeleteView(LoginRequiredMixin, DeleteView):
    model = Convocations
    success_url = reverse_lazy("convocations_list")
