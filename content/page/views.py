from django.http import HttpResponseNotFound
from django.shortcuts import redirect, render
from .services import PageService
from cms.views import CMSBaseView
from .forms import PageAddForm, PageEditForm
from .selectors import PageSelector


class CMSNavSideView(CMSBaseView):
    template_name = "cms/side.html"
    template_name_include = "page/page_add_form.html"
    form_class = PageAddForm

    def get(self, request, *args, **kwargs):
        pages = PageSelector.list_pages()
        context = {
            "pages": pages,
            "form": self.form_class,
            "template_name_include": self.template_name_include,
        }
        self.add_context(context)
        return render(request, self.get_template_to_render(), self.get_context())

class CMSNavTopView(CMSNavSideView):
    template_name_include = "page/edit_page_nav.html"

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        # page_id = self.kwargs.get("id")
        # if not page_id:
        #     return HttpResponseNotFound()
        #
        # page = PageSelector.get_page_by_id(page_pk=page_id, database="default")
        # self.add_context({"page": page})
        return render(request, self.get_template_to_render(), self.get_context())

class PageAddView(CMSNavSideView):
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
            self.clear_context(["errors"])

        self.add_context({"errors": form.errors})
        return redirect("pages")




class PageEditView(CMSNavTopView):
    form_class = PageEditForm
    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        # page_id = self.kwargs.get("id")
        # if not page_id:
        #     return HttpResponseNotFound()
        #
        # page = PageSelector.get_page_by_id(page_pk=page_id, database="default")
        # self.add_context({"page": page})
        return render(request, self.get_template_to_render(), self.get_context())



