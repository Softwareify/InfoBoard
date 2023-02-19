from django.shortcuts import render, redirect

from content.page.views import PageCMSBaseEditView
from content.page_structure.forms import PageStructureEditAddForm


class PageStructreEditView(PageCMSBaseEditView):
    template_name_form = "page_structure/edit_page_structure_form.html"
    template_name_addidtional_include = "page_structure/snippet_forms.html"
    form_class_snippet = SnippetEditAddForm
    form_class_page_structure = PageStructureEditAddForm

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        return render(request, self.get_template_to_render(), self.get_context())

    def post(self, request, *args, **kwargs):
        page = self.get_page_obj_by_pk_from_request(request, *args, **kwargs)
        page_structure = page.page_structure
        snippet_header = page_structure.header_snippet
        snippet_content = page_structure.content_snippet
        snippet_footer = page_structure.footer_snippet


        return redirect('page-structure', *args, **kwargs)
