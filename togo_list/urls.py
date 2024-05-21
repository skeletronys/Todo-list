from django.urls import path

from .views import (
    TagsListView,
    TagsUpdateView,
    TagsCreateView,
    TagsDeleteView,
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    toggle_task_status,
)

urlpatterns = [
    path("tags/", TagsListView.as_view(), name="tag-list-view"),
    path("tags/<int:pk>/update/", TagsUpdateView.as_view(), name="tag-update-view"),
    path("tags/create/", TagsCreateView.as_view(), name="tag-create-view"),
    path("tags/<int:pk>/delete/", TagsDeleteView.as_view(), name="tag-delete-view"),

    path('', TaskListView.as_view(), name='task-list-view'),
    path('create/', TaskCreateView.as_view(), name='task-create-view'),
    path('<int:pk>/update/', TaskUpdateView.as_view(), name='task-update-view'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete-view'),
    path('<int:pk>/toggle/', toggle_task_status, name='task-toggle-view'),
]


app_name = "togo"
