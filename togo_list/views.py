from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from togo_list.forms import TagForm
from togo_list.models import Tag


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
