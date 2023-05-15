from snippets.snippets import BaseSnippet


class VideoSnippetView(BaseSnippet):
    template_name = "video_snippet/video_snippet_desktop.html"

    def get_context(self):
        self.context["snippet"] = self.snippet_obj
        return self.context
