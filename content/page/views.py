from django.shortcuts import redirect, render
from .services import PageService
from cms.views import CMSBaseView
from .forms import PageForm
from .selectors import PageSelector
from datetime import datetime


class PageList(CMSBaseView):
    template_name = "cms/side.html"
    template_name_include = "page/page_form_template.html"
    form_class = PageForm

    def get(self, request, *args, **kwargs):
        pages = PageSelector.list_pages()
        context = {
            "pages": pages,
            "form": self.form_class,
            "template_name_include": self.template_name_include,
        }
        self.add_context(context)
        return render(request, self.get_template_to_render(), self.get_context())

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        page_data = {}

        if form.is_valid():
            cleaned_data = form.clean()
            page_data.update(
                {
                    "name": cleaned_data['name'],
                    "slug": cleaned_data['slug'],
                    "description": cleaned_data['description'],
                    "publish_from": cleaned_data["publish_from"],
                    "publish_to": cleaned_data["publish_to"],
                }
            )

            PageService.create_page(page_data=page_data, user=request.user)

        errors = form.errors
        self.add_context({"errors": errors})
        return redirect("pages")



