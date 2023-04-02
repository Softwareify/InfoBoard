from django.db import models

from modules.video.models import Video


class VideoSnippet(models.Model):
    pass


class VideoPositionSnippet(models.Model):
    order = models.IntegerField()
    video_snippet = models.ForeignKey(VideoSnippet, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE, null=True, blank=True)
