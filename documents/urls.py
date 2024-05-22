from django.urls import path

from example import views
from documents.views import (
    CondominiumDocumentsCreateView,
    CondominiumDocumentsDeleteView,
    CondominiumDocumentsListView,
    CondominiumDocumentsUpdateView,
    UserDocumentsCreateView,
    UserDocumentsDeleteView,
    UserDocumentsListView,
    UserDocumentsUpdateView
)

urlpatterns = [
    path("list", CondominiumDocumentsListView.as_view(), name="cond_docs_list"),
    path("create", CondominiumDocumentsCreateView.as_view(), name="cond_docs_create"),
    path("update/<int:pk>", CondominiumDocumentsUpdateView.as_view(), name="cond_docs_update"),
    path("delete/<int:pk>", CondominiumDocumentsDeleteView.as_view(), name="cond_docs_delete"),
    path("userdoclist", UserDocumentsListView.as_view(), name="user_docs_list"),
    path("userdoccreate", UserDocumentsCreateView.as_view(), name="user_docs_create"),
    path("userdocupdate/<int:pk>", UserDocumentsUpdateView.as_view(), name="user_docs_update"),
    path("userdocdelete/<int:pk>", UserDocumentsDeleteView.as_view(), name="user_docs_delete"),
]
