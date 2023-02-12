from django.contrib.auth import get_user_model
from django.db import models

from content.page_structure.models import PageStructure


class Page(models.Model):
    """Page class"""

    class StatusChoices(models.IntegerChoices):
        """Status choices"""

        NEW_DRAFT = 1, "Nowa kopia robocza"
        TO_PUBLISH = 2, "Do publikacji"
        PUBLISHED = 3, "Opublikowany"
        TO_ARCHIVE = 4, "Do archiwum"
        ARCHIVE = 5, "Archiwalny"

    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=200, blank=False, null=False, unique=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    status = models.IntegerField(
        choices=StatusChoices.choices,
        max_length=1,
        blank=False,
        null=False,
        default=StatusChoices.NEW_DRAFT,
    )
    description = models.CharField(max_length=500)
    created = models.DateTimeField(auto_created=True, auto_now=True)
    modified = models.DateTimeField(auto_created=True, auto_now=True)
    page_structure = models.OneToOneField(PageStructure, on_delete=models.CASCADE)
    publish_from = models.DateTimeField()
    publish_to = models.DateTimeField(null=True, blank=True)

    @property
    def publish_from_iso(self):
        return self.publish_from.isoformat()[:-9]

    @property
    def publish_to_iso(self):
        if not self.publish_to:
            return None
        return self.publish_to.isoformat()[:-9]
