from django import forms

from modules.video.models import Video
from snippets.video_snippet.models import VideoSnippet, VideoPositionSnippet


class VideoPositionSnippetForm(forms.ModelForm):
    class Meta:
        model = VideoPositionSnippet
        fields = "__all__"

        widgets = {
            "order": forms.HiddenInput(),
            "video_snippet": forms.HiddenInput(),
        }


class VideoSnippetForm(forms.ModelForm):
    template_name_p = "video_snippet/video_snippet_form.html"

    class Meta:
        model = VideoSnippet
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        videos = Video.objects.all()
        for i, video in enumerate(videos):
            video_position = VideoPositionSnippet.objects.filter(
                video_snippet_id=self.instance.id, order=i
            ).first()
            video_position_form = VideoPositionSnippetForm(instance=video_position)
            for field in video_position_form.fields:
                self.fields[f"{field}_{i}"] = video_position_form.fields[field]
                self.fields[f"{field}_{i}"].required = False
                if field == "order":
                    self.fields[f"{field}_{i}"].initial = i
                    if video_position:
                        self.fields[f"{field}_{i}"].initial = video_position.order
                if field == "video_snippet":
                    self.fields[f"{field}_{i}"].initial = self.instance.id
                    if video_position:
                        self.fields[
                            f"{field}_{i}"
                        ].initial = video_position.video_snippet.id
                if field == "video":
                    if video_position and video_position.video:
                        self.fields[f"{field}_{i}"].initial = video_position.video.id

    def save(self, commit=True, *args, **kwargs):
        saved_instance = super().save(*args, **kwargs)
        keys = self.cleaned_data.keys()
        for i in range(0, len(keys) // 3):
            new_data = {
                key.split(f"_{i}")[0]: self.cleaned_data.get(key)
                for key in keys
                if key.endswith(f"_{i}")
            }
            form = VideoPositionSnippetForm(data=new_data)
            if new_data.get(f"video_snippet") and str(new_data.get(f"order")):
                video_position = VideoPositionSnippet.objects.filter(
                    video_snippet_id=new_data.get("video_snippet"),
                    order=new_data.get("order"),
                ).first()
                form = VideoPositionSnippetForm(data=new_data, instance=video_position)
            if form.is_valid():
                form.save(*args, **kwargs)

        return saved_instance
