from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import ServiceOrders


class ServiceOrdersListView(LoginRequiredMixin, ListView):
    model = ServiceOrders

class ServiceOrdersCreateView(LoginRequiredMixin, CreateView):
    model = ServiceOrders
    fields = ["title", "description", "image_url"]
    success_url = reverse_lazy("service_orders_list")
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ServiceOrdersCreateView, self).form_valid(form)

class ServiceOrdersUpdateView(LoginRequiredMixin, UpdateView):
    model = ServiceOrders
    fields = ["title", "description", "image_url"]
    success_url = reverse_lazy("service_orders_list")
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ServiceOrdersUpdateView, self).form_valid(form)

class ServiceOrdersDeleteView(LoginRequiredMixin, DeleteView):
    model = ServiceOrders
    success_url = reverse_lazy("service_orders_list")
