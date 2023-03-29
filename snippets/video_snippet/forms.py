from django import forms

from snippets.video_snippet.models import VideoSnippet


class VideoSnippetForm(forms.ModelForm):
    template_name_p = "video_snippet/video_snippet_form.html"

    class Meta:
        model = VideoSnippet
        fields = "__all__"
