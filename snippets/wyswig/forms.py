import random

from ckeditor.widgets import CKEditorWidget
from django import forms

from .models import WyswigSnippet


class WyswigSnippetForm(forms.ModelForm):
    template_name_p = 'wyswig/wyswig_form.html'
    content = forms.CharField(widget=CKEditorWidget(), required=False)

    class Meta:
        model = WyswigSnippet
        fields = "__all__"