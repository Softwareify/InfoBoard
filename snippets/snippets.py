from django.template.loader import render_to_string


class BaseSnippet:
    template_name = None
    context = {}

    def __init__(self, snippet_obj):
        self.snippet_obj = snippet_obj

    def get_context(self):
        return self.context

    def render(self):
        return render_to_string(self.template_name, self.get_context())
