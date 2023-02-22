from django.shortcuts import redirect, render

from content.page.views import PageCMSBaseEditView
from content.page_structure.services import PageStructureService
from snippets.services import SnippetService


class PageStructreEditView(PageCMSBaseEditView):
    template_name_form = "page_structure/edit_page_structure_form.html"
    template_name_addidtional_include = "page_structure/snippet_forms.html"

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        return render(request, self.get_template_to_render(), self.get_context())

    def post(self, request, *args, **kwargs):
        data = request.POST
        print(data)
        page = self.get_page_obj_by_pk_from_request(request, *args, **kwargs)
        PageStructureService.update_structure(
            page_structure=page.page_structure, updated_data=data
        )
        print(SnippetService.get_snippets_info(data=data))
        return redirect("page-structure", *args, **kwargs)
