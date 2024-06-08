from django.conf import settings

from snippets.snippets import BaseSnippet


class VideoSnippetView(BaseSnippet):
    template_name = "video_snippet/video_snippet_desktop.html"

    def get_context(self):
        self.context["snippet"] = self.snippet_obj
        self.context["IS_CMS"] = settings.IS_CMS
        return self.context
