from django.urls import path

from boards.views import (
    NoticeBoardListView,
    NoticeBoardCreateView,
    NoticeBoardDeleteView,
    NoticeBoardUpdateView,
    SugestionBoardListView,
    SugestionBoardCreateView,
    SugestionBoardDeleteView,
    SugestionBoardUpdateView,
    EventBoardListView,
    EventBoardCreateView,
    EventBoardUpdateView,
    EventBoardDeleteView
)

urlpatterns = [
    path("notice-list", NoticeBoardListView.as_view(), name="notice_boards_list"),
    path("notice-create", NoticeBoardCreateView.as_view(), name="notice_boards_create"),
    path("notice-update/<int:pk>", NoticeBoardUpdateView.as_view(), name="notice_boards_update"),
    path("notice-delete/<int:pk>", NoticeBoardDeleteView.as_view(), name="notice_boards_delete"),
    path("sugestion-list", SugestionBoardListView.as_view(), name="sugestion_boards_list"),
    path("sugestion-create", SugestionBoardCreateView.as_view(), name="sugestion_boards_create"),
    path("sugestion-update/<int:pk>", SugestionBoardUpdateView.as_view(), name="sugestion_boards_update"),
    path("sugestion-delete/<int:pk>", SugestionBoardDeleteView.as_view(), name="sugestion_boards_delete"),
    path("event-list", EventBoardListView.as_view(), name="event_boards_list"),
    path("event-create", EventBoardCreateView.as_view(), name="event_boards_create"),
    path("event-update/<int:pk>", EventBoardUpdateView.as_view(), name="event_boards_update"),
    path("event-delete/<int:pk>", EventBoardDeleteView.as_view(), name="event_boards_delete"),
]
