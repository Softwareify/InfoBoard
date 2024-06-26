import os.path

import ffmpeg
from django.db import models

from modules.video.models import Video
from varnish.services import VarnishService


class VideoSnippet(models.Model):
    pass

    def publish(self):
        self.save(using="public")
        for position_video_snippet in VideoPositionSnippet.objects.filter(
            video_snippet_id=self.id
        ):
            position_video_snippet.save(using="public")
        clips_input = [
            ffmpeg.input(video_position.video.filepath.path)
            for video_position in self.positions.all().order_by("-order")
            if hasattr(getattr(video_position, "video"), "filepath")
        ]
        if not clips_input:
            return
        merge_clips_inputs = ffmpeg.concat(*clips_input)
        if not os.path.exists("./mediafiles/videos_rendered"):
            os.makedirs("./mediafiles/videos_rendered")
        merge_clips_output = merge_clips_inputs.output(
            f"./mediafiles/videos_rendered/{self.id}.mp4", format="mp4"
        )
        merge_clips_output.run(overwrite_output=True)
        VarnishService().purge_path(path=f"/mediafiles/videos_rendered/{self.id}.mp4")

    def unpublish(self):
        if os.path.exists(f"./mediafiles/videos_rendered/{self.id}.mp4"):
            os.remove(f"./mediafiles/videos_rendered/{self.id}.mp4")
        self.delete(using="public")


class VideoPositionSnippet(models.Model):
    order = models.IntegerField()
    video_snippet = models.ForeignKey(
        VideoSnippet, on_delete=models.CASCADE, related_name="positions"
    )
    video = models.ForeignKey(Video, on_delete=models.CASCADE, null=True, blank=True)
