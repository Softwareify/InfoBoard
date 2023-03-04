from django.forms import ModelForm

from snippets.models import BaseSnippet


class BaseSnippetForm(ModelForm):
    class Meta:
        model = BaseSnippet
        fields = ["type", "snippet_id"]
