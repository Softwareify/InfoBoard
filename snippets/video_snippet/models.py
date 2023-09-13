from django.db import models

from modules.video.models import Video


class VideoSnippet(models.Model):
    pass

    def publish(self):
        self.save(using="public")
        for position_video_snippet in VideoPositionSnippet.objects.filter(
            video_snippet_id=self.id
        ):
            position_video_snippet.save(using="public")


class VideoPositionSnippet(models.Model):
    order = models.IntegerField()
    video_snippet = models.ForeignKey(
        VideoSnippet, on_delete=models.CASCADE, related_name="positions"
    )
    video = models.ForeignKey(Video, on_delete=models.CASCADE, null=True, blank=True)
