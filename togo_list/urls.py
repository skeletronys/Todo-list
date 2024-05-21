from django.urls import path

from .views import TagsListView

urlpatterns = [
    path("", TagsListView.as_view(), name="tag-list-view")
]
