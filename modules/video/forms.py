from django import forms

from modules.video.models import Video


class VideoAddForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = "__all__"
