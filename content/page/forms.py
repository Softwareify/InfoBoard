from datetime import datetime

from django.forms import ModelForm

from .models import Page


class PageForm(ModelForm):
    class Meta:
        model = Page
        exclude = ("status", "created", "modified", "page_structure")
