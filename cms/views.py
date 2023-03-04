from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View


class CMSBaseView(LoginRequiredMixin, View):
    """Base view for all views in CMS"""

    login_url = "auth/login/"
    template_name = "cms/right_content.html"
    template_name_form = None
    template_name_top_nav = None
    template_name_addidtional_include = None
    context = {}

    def add_context(self, context_updated: dict):
        """Method for add context"""
        self.context.update(context_updated)

    def clear_context(self, keys: list):
        """Method for clear context"""
        for key in keys:
            if self.context.get(key):
                self.context.pop(key)

    def get_context(self, *args, **kwargs):
        """Method for get context"""
        return self.context

    def get_template_to_render(self, *args, **kwargs):
        """Method for get template to render"""
        return self.template_name

    def get(self, request, *args, **kwargs):
        """Base method for GET request"""
        self.add_context(
            {
                "template_name_form": self.template_name_form,
                "template_name_top_nav": self.template_name_top_nav,
                "template_name_addidtional_include": self.template_name_addidtional_include,
            }
        )
        if request.build_absolute_uri() != request.META.get("HTTP_REFERER"):
            self.clear_context(["errors"])


class CMSView(CMSBaseView):
    """Base CMS View"""

    pass


class CMSTopNavView(CMSView):
    """View CMS for top nav"""

    template_name_top_nav = "cms/top_nav.html"
