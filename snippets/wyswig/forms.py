import random

from ckeditor.widgets import CKEditorWidget
from django import forms

from .models import WyswigSnippet


class WyswigSnippetForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget(), required=False)

    class Meta:
        model = WyswigSnippet
        fields = "__all__"
