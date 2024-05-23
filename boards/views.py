from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import NoticeBoard, EventBoard, SugestionBoard, UsefulPhonesBoard


class NoticeBoardListView(LoginRequiredMixin, ListView):
    model = NoticeBoard

class NoticeBoardCreateView(LoginRequiredMixin, CreateView):
    model = NoticeBoard
    fields = ["title", "description", "doc_url"]
    success_url = reverse_lazy("notice_boards_list")

class NoticeBoardUpdateView(LoginRequiredMixin, UpdateView):
    model = NoticeBoard
    fields = ["title", "description", "doc_url"]
    success_url = reverse_lazy("notice_boards_list")

class NoticeBoardDeleteView(LoginRequiredMixin, DeleteView):
    model = NoticeBoard
    success_url = reverse_lazy("notice_boards_list")
