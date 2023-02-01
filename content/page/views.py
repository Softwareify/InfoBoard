from django.shortcuts import render
from cms.views import CMSBaseView
from .selectors import PageSelector
from django.shortcuts import render
from .forms import PageForm


class PageSnippetsList(CMSBaseView):
    pages = PageSelector.list_pages()
    template_name = 'cms/side.html'
    template_name_include = 'page/page_form_template.html'
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
        print(self.cleaned_data())
        pass