from django.db import models

from snippets.wyswig.models import WyswigSnippet


class Snippet(models.Model):
    """Base snippet model for other snippets"""

    class TypeSnippetChoices(models.TextChoices):
        """Type snippet choices"""

        TYPE_SNIPPET_CHOICES = "wyswig_snippet", "Wyswig"

    created = models.DateTimeField(auto_created=True)
    modified = models.DateTimeField(auto_created=True, auto_now=True)
    type = models.CharField(
        max_length=200,
        choices=TypeSnippetChoices.choices,
        blank=False,
        null=False,
    )
    snippet_id = models.IntegerField(null=False, blank=False)
