from snippets.snippets import BaseSnippet


class HtmlSnippetView(BaseSnippet):
    template_name = "html/html_snippet_desktop.html"

    def get_context(self):
        self.context["snippet"] = self.snippet_obj
        return self.context
