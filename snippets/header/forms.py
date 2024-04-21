from django import forms

from snippets.header.models import HeaderSnippet


class HeaderSnippetForm(forms.ModelForm):
    template_name_p = "header/header_form.html"

    class Meta:
        model = HeaderSnippet
        fields = "__all__"
