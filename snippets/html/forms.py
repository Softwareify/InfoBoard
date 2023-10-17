from django import forms

from snippets.html.models import HtmlSnippet


class HtmlSnippetForm(forms.ModelForm):
    template_name_p = "html/html_form.html"

    class Meta:
        model = HtmlSnippet
        fields = "__all__"
