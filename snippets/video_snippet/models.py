from django.db import models

from modules.video.models import Video


class VideoSnippet(models.Model):
    videos = models.ManyToManyField(Video, null=True, blank=True)
