from django.shortcuts import render
from django.views import generic

from togo_list.models import Tag


class TagsListView(generic.ListView):
    model = Tag
    context_object_name = "tag_list"
    template_name = "togo/tag_list.html"
