import os.path

from django.http import Http404, HttpResponse
from django.shortcuts import redirect
from moviepy.editor import *

from snippets.video_snippet.models import VideoSnippet


class VideoPreviewMergeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.path
        if "/mediafiles/videos_rendered/preview/" in path:
            try:
                video_snippet_pk = path.split("/")[-1].split(".")[0]
                video_snippet = VideoSnippet.objects.prefetch_related("positions").get(
                    id=video_snippet_pk
                )
                if not video_snippet:
                    return HttpResponse(status=404)
                video_positions = video_snippet.positions.all().order_by("-order")
                clips = [
                    VideoFileClip(video_position.video.filepath.path)
                    for video_position in video_positions
                    if hasattr(getattr(video_position, "video"), "filepath")
                ]
                merged_clips = concatenate_videoclips(clips)
                if not os.path.exists("./mediafiles/videos_rendered_preview"):
                    os.makedirs("./mediafiles/videos_rendered_preview")
                merged_clips.write_videofile(
                    f"./mediafiles/videos_rendered_preview/{video_snippet_pk}.mp4"
                )
                video_response = open(
                    f"./mediafiles/videos_rendered_preview/{video_snippet_pk}.mp4"
                )
                os.remove(
                    f"./mediafiles/videos_rendered_preview/{video_snippet_pk}.mp4"
                )
            except Exception as e:
                raise Http404(e)
            return HttpResponse(video_response.buffer, content_type="video/mp4")

        return self.get_response(request)


class AuthenicateRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated and not request.path == "/auth/login/":
            return redirect("login")
        return self.get_response(request)
