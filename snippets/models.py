from django.db import models

from custom.utils import (
    get_snippet_cls,
    get_snippet_form,
    get_snippet_service,
    get_snippet_view,
)


class BaseSnippet(models.Model):
    """Base snippet model for other snippets"""

    class TypeSnippetChoices(models.TextChoices):
        """Type snippet choices"""

        WYSWIG = "wyswig_snippet", "Wyswig"
        VIDEO = "video_snippet", "Video"
        HTML = "html_snippet", "HTML"

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

    @property
    def type_label(self):
        return self.TypeSnippetChoices(self.type).label

    @property
    def snippet_view(self):
        return get_snippet_view(self.snippet)

    def publish(self):
        if self.snippet:
            self.snippet.publish()
        self.save(using="public")
