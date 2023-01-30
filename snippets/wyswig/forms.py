from ckeditor.widgets import CKEditorWidget
from django import forms
from .models import WyswigSnippet

class CMSWyswigForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = WyswigSnippet
        fields = "__all__"