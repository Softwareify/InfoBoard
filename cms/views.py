from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

class CMSBaseView(LoginRequiredMixin, View):
    login_url = 'auth/login/'
    template_name = None
    context = {}

    def add_context(self, context_updated: dict):
        self.context.update(context_updated)

    def clear_context(self, keys: list):
        for key in keys:
            if self.context.get(key):
                self.context.pop(key)
    def get_context(self, *args, **kwargs):
        return self.context

    def get_template_to_render(self, *args, **kwargs):
        return self.template_name
