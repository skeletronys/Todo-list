from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from togo_list.forms import TagForm, TaskForm
from togo_list.models import Tag, Task


class TagsListView(generic.ListView):
    model = Tag
    context_object_name = "tag_list"
    template_name = "togo/tag_list.html"


class TagsCreateView(generic.CreateView):
    model = Tag
    form_class = TagForm
    template_name = "togo/tag_form.html"
    success_url = reverse_lazy("togo:tag-list-view")


class TagsUpdateView(generic.UpdateView):
    model = Tag
    form_class = TagForm
    template_name = "togo/tag_form.html"
    success_url = reverse_lazy("togo:tag-list-view")


class TagsDeleteView(generic.DeleteView):
    model = Tag
    template_name = "togo/tag_confirm_delete.html"
    success_url = reverse_lazy("togo:tag-list-view")


class TaskListView(generic.ListView):
    model = Task
    template_name = "togo/task_list.html"
    context_object_name = "tasks"


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = "togo/task_form.html"
    success_url = reverse_lazy("togo:task-list-view")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "togo/task_form.html"
    success_url = reverse_lazy("togo:task-list-view")


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "togo/task_confirm_delete.html"
    success_url = reverse_lazy("togo:task-list-view")


def toggle_task_status(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = not task.is_completed
    task.save()
    return redirect("togo:task-list-view")
