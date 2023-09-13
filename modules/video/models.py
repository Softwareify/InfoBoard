import uuid

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


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

    def __str__(self):
        return self.name


@receiver(post_save, sender=Video)
def post_save(*_args, **_kwargs):
    instance = _kwargs.get("instance", {})
    if instance._state.db == "default":
        instance.save(using="public")
