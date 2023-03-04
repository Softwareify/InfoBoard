from django.shortcuts import redirect, render

from content.page.views import PageCMSBaseEditView
from content.page_structure.services import PageStructureService
from snippets.services import BaseSnippetService


class PageStructreEditView(PageCMSBaseEditView):
    template_name_form = "page_structure/edit_page_structure_form.html"
    template_name_addidtional_include = "page_structure/snippet_forms.html"

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        return render(request, self.get_template_to_render(), self.get_context())
