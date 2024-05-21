from django.urls import path

from .views import (
    TagsListView,
    TagsUpdateView,
    TagsCreateView,
    TagsDeleteView,
)

urlpatterns = [
    path("", TagsListView.as_view(), name="tag-list-view"),
    path("tags/<int:pk>/update/", TagsUpdateView.as_view(), name="tag-update-view"),
    path("tags/create/", TagsCreateView.as_view(), name="tag-create-view"),
    path("tags/<int:pk>/delete/", TagsDeleteView.as_view(), name="tag-delete-view"),
]


app_name = "togo"
