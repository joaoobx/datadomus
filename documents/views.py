from django.http import JsonResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin

from example.serializer import ItemSerializer

from .models import CondominiumDocuments, UserDocuments


class CondominiumDocumentsListView(LoginRequiredMixin, ListView):
    model = CondominiumDocuments

class CondominiumDocumentsCreateView(LoginRequiredMixin, CreateView):
    model = CondominiumDocuments
    fields = ["doc_name", "doc_url"]
    success_url = reverse_lazy("cond_docs_list")

class CondominiumDocumentsUpdateView(LoginRequiredMixin, UpdateView):
    model = CondominiumDocuments
    fields = ["doc_name", "doc_url"]
    success_url = reverse_lazy("cond_docs_list")

class CondominiumDocumentsDeleteView(LoginRequiredMixin, DeleteView):
    model = CondominiumDocuments
    success_url = reverse_lazy("cond_docs_list")

class UserDocumentsListView(LoginRequiredMixin, ListView):
    model = UserDocuments
    def form_valid(self, form):
        form.instance.user = self.request.user.id
        return super(UserDocuments, self).form_valid(form)

class UserDocumentsCreateView(LoginRequiredMixin, CreateView):
    model = UserDocuments
    fields = ["doc_name", "doc_url"]
    success_url = reverse_lazy("user_docs_list")
    def form_valid(self, form):
        form.instance.user = self.request.user.id
        return super(UserDocuments, self).form_valid(form)

class UserDocumentsUpdateView(LoginRequiredMixin, UpdateView):
    model = UserDocuments
    fields = ["doc_name", "doc_url"]
    success_url = reverse_lazy("user_docs_list")
    def form_valid(self, form):
        form.instance.user = self.request.user.id
        return super(UserDocuments, self).form_valid(form)

class UserDocumentsDeleteView(LoginRequiredMixin, DeleteView):
    model = UserDocuments
    success_url = reverse_lazy("user_docs_list")
    def form_valid(self, form):
        form.instance.user = self.request.user.id
        return super(UserDocuments, self).form_valid(form)
