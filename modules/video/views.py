from django.shortcuts import redirect, render

from modules.video.forms import VideoAddForm
from modules.views import VideoModuleCMSBaseView


class VideoModuleCMSAddView(VideoModuleCMSBaseView):
    template_name_form = "video/video_add_form.html"
    form_class = VideoAddForm

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        self.clear_context(["active_page"])
        return render(request, self.get_template_to_render(), self.get_context())

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
        self.add_context({"errors": form.errors})
        return redirect("videos")
