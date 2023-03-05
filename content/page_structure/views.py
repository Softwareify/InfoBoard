from django.shortcuts import render

from content.page.views import PageCMSBaseEditView


class PageStructreEditView(PageCMSBaseEditView):
    template_name_form = "page_structure/edit_page_structure_form.html"

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        return render(request, self.get_template_to_render(), self.get_context())
