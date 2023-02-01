from django.forms import ModelForm
from .models import Page
from datetime import datetime

class PageForm(ModelForm):
    class Meta:
        model = Page
        exclude = ("status", "created", "modified", "created", "page_structure")