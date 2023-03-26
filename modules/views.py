from django.shortcuts import render

from cms.views import CMSBaseView
from modules.video.selectors import VideoSelector


class VideoModuleCMSBaseView(CMSBaseView):
    def get(self, request, *args, **kwargs):
        self.clear_context(["pages"])
        videos = VideoSelector.get_all()
        self.add_context({"videos": videos})
        super().get(request, *args, **kwargs)
        return render(request, self.get_template_to_render(), self.get_context())
