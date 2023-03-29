from django import forms
from tinymce.widgets import TinyMCE

from .models import WyswigSnippet


class WyswigSnippetForm(forms.ModelForm):
    template_name_p = "wyswig/wyswig_form.html"
    content = forms.CharField(
        widget=TinyMCE(attrs={"cols": 80, "rows": 30}), required=False
    )

    class Meta:
        model = WyswigSnippet
        fields = "__all__"
