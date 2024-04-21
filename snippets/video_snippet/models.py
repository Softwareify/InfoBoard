import ffmpeg
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
        clips_input = [
            ffmpeg.input(video_position.video.filepath.path)
            for video_position in self.positions.all().order_by("-order")
            if hasattr(getattr(video_position, "video"), "filepath")
        ]
        merge_clips_inputs = ffmpeg.concat(*clips_input)
        merge_clips_output = merge_clips_inputs.output(
            f"./mediafiles/videos_rendered/{self.id}.mp4", format="mp4"
        )
        merge_clips_output.run(overwrite_output=True)


class VideoPositionSnippet(models.Model):
    order = models.IntegerField()
    video_snippet = models.ForeignKey(
        VideoSnippet, on_delete=models.CASCADE, related_name="positions"
    )
    video = models.ForeignKey(Video, on_delete=models.CASCADE, null=True, blank=True)
