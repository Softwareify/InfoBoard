from django.db import models

from snippets.utils import get_ref_snippet_cls


class Snippet(models.Model):
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
    def ref_snippet_obj(self):
        ref_snippet_cls = get_ref_snippet_cls(self.type)
        try:
            return ref_snippet_cls.objects.get(id=self.snippet_id)
        except ref_snippet_cls.DoesNotExist:
            return None
