from django.db import models

from snippets.models import Snippet


class PageStructure(models.Model):
    """Page structure class"""

    header_snippet = models.ForeignKey(
        Snippet,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name="header_snippet",
    )
    content_snippet = models.ForeignKey(
        Snippet,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name="content_snippet",
    )
    footer_snippet = models.ForeignKey(
        Snippet,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name="footer_snippet",
    )
