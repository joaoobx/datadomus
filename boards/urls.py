from django.urls import path

from example import views
from boards.views import (
    NoticeBoardListView,
    NoticeBoardCreateView,
    NoticeBoardDeleteView,
    NoticeBoardUpdateView
)

urlpatterns = [
    path("list", NoticeBoardListView.as_view(), name="notice_boards_list"),
    path("create", NoticeBoardCreateView.as_view(), name="notice_boards_create"),
    path("update/<int:pk>", NoticeBoardUpdateView.as_view(), name="notice_boards_update"),
    path("delete/<int:pk>", NoticeBoardDeleteView.as_view(), name="notice_boards_delete"),
]
