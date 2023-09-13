from django.db import models


class Task(models.Model):
    class TypePublication(models.TextChoices):
        PAGE_PUBLISH = "page_publish", "page_publish"
        PAGE_ARCHIVE = "page_archive", "page_archive"

    type_publication = models.CharField(choices=TypePublication.choices, max_length=32)
    object_id = models.IntegerField()
    due_date = models.DateTimeField(null=True, blank=True)
    execution_date = models.DateTimeField(null=True, blank=True)
    retries = models.IntegerField(default=0)
