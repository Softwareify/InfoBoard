from django.db import models

from snippets.utils import (get_snippet_cls, get_snippet_form,
                            get_snippet_service)


class BaseSnippet(models.Model):
    """Base snippet model for other snippets"""

    class TypeSnippetChoices(models.TextChoices):
        """Type snippet choices"""

        TYPE_SNIPPET_CHOICES = "wyswig_snippet", "Wyswig"

    created = models.DateTimeField(auto_created=True, auto_now=True)
    modified = models.DateTimeField(auto_created=True, auto_now=True)
    type = models.CharField(
        max_length=200,
        choices=TypeSnippetChoices.choices,
        blank=True,
        null=True,
    )
    snippet_id = models.IntegerField(null=True, blank=True)

    @property
    def snippet(self):
        snippet_cls = get_snippet_cls(self.type)
        try:
            return snippet_cls.objects.get(id=self.snippet_id)
        except Exception:
            return None

    @property
    def snippet_form(self):
        snippet_form = get_snippet_form(self.type)
        if self.snippet and snippet_form:
            return snippet_form(instance=self.snippet)
        return None

    @property
    def snippet_service(self):
        return get_snippet_service(self.type)
