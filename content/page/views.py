from django.shortcuts import redirect, render
from .services import PageService
from cms.views import CMSBaseView
from .forms import PageForm
from .selectors import PageSelector
from datetime import datetime


class PageSnippetsList(CMSBaseView):
    pages = PageSelector.list_pages()
    template_name = "cms/side.html"
    template_name_include = "page/page_form_template.html"
    form_class = PageForm

    def get(self, request, *args, **kwargs):
        context = {
            "pages": self.pages,
            "form": self.form_class,
            "template_name_include": self.template_name_include,
        }
        self.add_context(context)
        return render(request, self.get_template_to_render(), self.get_context())

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        page_data = {}

        if form.is_valid:
            name = form.data["name"]
            slug = form.data["slug"]
            description = form.data["description"]
            publish_from = form.data["publish_from"]
            publish_to = form.data["publish_to"]
            page_data.update(
                {
                    "name": name,
                    "slug": slug,
                    "description": description,
                    "publish_from": datetime.strptime(publish_from, "%Y-%m-%dT%H:%M"),
                    "publish_to": datetime.strptime(publish_to, "%Y-%m-%dT%H:%M"),
                }
            )

            PageService.create_page(page_data=page_data, user=request.user)

        return redirect("pages")
