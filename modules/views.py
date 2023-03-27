from django.http import HttpResponseNotFound
from django.shortcuts import render

from cms.views import CMSBaseView
from modules.video.selectors import VideoSelector


class VideoModuleCMSBaseView(CMSBaseView):
    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        self.clear_context(["pages"])
        videos = VideoSelector.get_all()
        self.add_context({"videos": videos})

    def get_video_obj_by_pk_from_request(self, *args, **kwargs):
        video_id = self.kwargs.get("pk")
        if not video_id:
            return HttpResponseNotFound()
        return VideoSelector.get(video_id)
