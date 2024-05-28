from django.db import models

from snippets.models import BaseSnippet


class PageStructure(models.Model):
    """Page structure class"""

    header_snippet = models.ForeignKey(
        BaseSnippet,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name="header_snippet",
    )
    content_snippet = models.ForeignKey(
        BaseSnippet,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name="content_snippet",
    )
    footer_snippet = models.ForeignKey(
        BaseSnippet,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name="footer_snippet",
    )

    def publish(self):
        self.header_snippet.publish()
        self.content_snippet.publish()
        self.footer_snippet.publish()
        self.save(using="public")

    def unpublish(self):
        self.delete(using="public")
        self.header_snippet.unpublish()
        self.content_snippet.unpublish()
        self.footer_snippet.unpublish()
