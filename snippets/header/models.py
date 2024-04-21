from django.db import models


class HeaderSnippet(models.Model):
    """Html snippet model"""

    class HxChoices(models.TextChoices):
        H1 = "h1", "H1"
        H2 = "h2", "H2"
        H3 = "h3", "H3"
        H4 = "h4", "H4"
        H5 = "h5", "H5"
        H6 = "h6", "H6"

    hx = models.CharField(
        choices=HxChoices.choices, default=HxChoices.H1, max_length=10, blank=True
    )
    content = models.TextField(null=True, blank=True, default="")

    def publish(self):
        self.save(using="public")

    @property
    def display_number(self):
        if self.hx:
            return int(self.hx[-1])
        return None
