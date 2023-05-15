from snippets.snippets import BaseSnippet
from snippets.wyswig.models import WyswigSnippet


class WyswigSnippetView(BaseSnippet):
    template_name = "wyswig/wyswig_desktop.html"
    model = WyswigSnippet

    def get_context(self):
        self.context = {"content": self.snippet_obj.content}
        return self.context
