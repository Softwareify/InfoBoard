from snippets.snippets import BaseSnippet


class HeaderSnippetView(BaseSnippet):
    template_name = "header/header_snippet_desktop.html"

    def get_context(self):
        self.context["snippet"] = self.snippet_obj
        return self.context
