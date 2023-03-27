import uuid
from uuid import uuid4

from django.db import models


class Video(models.Model):
    filepath = models.FileField(upload_to="./videos")
    name = models.CharField(max_length=250)

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        if not self.id:
            filepath = self.filepath
            ext = filepath.name.lower().split(".")[-1]
            filepath.name = f"{uuid.uuid4()}.{ext}"
        super().save(force_insert, force_update, using, update_fields)
