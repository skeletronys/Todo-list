from django import forms

from togo_list.models import Tag


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = "__all__"

