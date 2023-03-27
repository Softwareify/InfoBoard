from django.shortcuts import redirect, render

from modules.video.forms import VideoForm
from modules.video.services import VideoService
from modules.views import VideoModuleCMSBaseView


class VideoModuleCMSAddView(VideoModuleCMSBaseView):
    template_name_form = "video/video_add_form.html"
    form_class = VideoForm
    service = VideoService()

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        self.clear_context(["active_page"])
        return render(request, self.get_template_to_render(), self.get_context())

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST, files=request.FILES)
        if form.is_valid():
            self.service.save_video(
                filepath=form.cleaned_data["filepath"], name=form.cleaned_data["name"]
            )
        self.add_context({"errors": form.errors})
        return redirect("videos")


class VideoModuleCMSEditView(VideoModuleCMSBaseView):
    template_name_form = "video/video_edit_form.html"
    form_class = VideoForm
    service = VideoService()

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        video = self.get_video_obj_by_pk_from_request(request, *args, **kwargs)
        self.add_context({"video": video, "active_page": video.id})
        return render(request, self.get_template_to_render(), self.get_context())

    def post(self, request, *args, **kwargs):
        video = self.get_video_obj_by_pk_from_request(request, *args, **kwargs)
        form = self.form_class(data=request.POST, files=request.FILES, instance=video)
        if form.is_valid():
            if not self.service.validate_filepath(
                filepath_cleaned=form.cleaned_data["filepath"]
            ):
                self.add_context({"errors": {"Plik ": "Nie poprawny format filmu!"}})
                return redirect("video-edit", *args, **kwargs)

            self.service.update_video(
                instance=video,
                filepath=form.cleaned_data["filepath"],
                name=form.cleaned_data["name"],
            )
        self.add_context({"errors": form.errors})
        return redirect("video-edit", *args, **kwargs)
