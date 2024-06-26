from django.db import models

from custom import utils


class BaseSnippet(models.Model):
    """Base snippet model for other snippets"""

    class TypeSnippetChoices(models.TextChoices):
        """Type snippet choices"""

        WYSWIG = "wyswig_snippet", "Wyswig"
        VIDEO = "video_snippet", "Video"
        HTML = "html_snippet", "HTML"
        HEADER = "header_snippet", "Header"

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
        snippet_cls = utils.get_snippet_cls(self.type)
        try:
            return snippet_cls.objects.get(id=self.snippet_id)
        except Exception:
            return None

    @property
    def snippet_form(self):
        snippet_form = utils.get_snippet_form(self.type)
        if self.snippet and snippet_form:
            return snippet_form(instance=self.snippet)
        return None

    @property
    def snippet_service(self):
        return utils.get_snippet_service(self.type)

    @property
    def type_label(self):
        return self.TypeSnippetChoices(self.type).label

    @property
    def snippet_view(self):
        return utils.get_snippet_view(self.snippet)

    def publish(self):
        if self.snippet:
            self.snippet.publish()
        self.save(using="public")

    def unpublish(self):
        if self.snippet:
            self.snippet.unpublish()
        self.delete(using="public")
