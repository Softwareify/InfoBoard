from django.http import HttpResponse

from snippets.video_snippet.models import VideoSnippet, VideoPositionSnippet
from moviepy.editor import *


class VideoMergeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.path
        if path.split("/")[-2] == "mvideo":
            video_snippet_pk = path.split("/")[-1].split('.')[0]
            video_snippet_qs = VideoSnippet.objects.get(id=video_snippet_pk)
            video_positions = VideoPositionSnippet.objects.filter(
                video_snippet_id=video_snippet_qs.id
            ).order_by("-order")
            clips = [VideoFileClip(video_position.video.filepath.path) for video_position in video_positions]
            merged_clips = concatenate_videoclips(clips)
            merged_clips.write_videofile(f"./mediafiles/videos_rendered/{video_snippet_pk}.mp4")
            video_response = open(f"./mediafiles/videos_rendered/{video_snippet_pk}.mp4")
            return HttpResponse(video_response.buffer, content_type="video/mp4")

        return self.get_response(request)
