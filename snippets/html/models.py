from django.db import models


class HtmlSnippet(models.Model):
    """Html snippet model"""

    html = models.TextField(null=True, blank=True, default="")

    def publish(self):
        self.save(using="public")
