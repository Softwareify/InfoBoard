from django.db import models


class BaseSnippet(models.Model):
    class TypeSnippetChoices(models.Choices):
        TYPE_SNIPPET_CHOICES = (
            ("wyswig_snippet", "Wyswig")
        )

    created = models.DateTimeField(auto_created=True)
    modified = models.DateTimeField(auto_created=True, auto_now=True)
    type = models.CharField(max_length=200, choices=TypeSnippetChoices.TYPE_SNIPPET_CHOICES, blank=False, null=False)
    snippet = models.OneToOneField()