from django.shortcuts import render
from cms.views import CMSBaseView
from .selectors import PageSelector
from django.shortcuts import render
from .forms import PageForm
from django.shortcuts import redirect
from datetime import datetime
from .models import Page
from content.page_structure.models import PageStructure


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
        print (context)
        self.add_context(context)
        return render(request, self.get_template_to_render(), self.get_context())

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid:
            name = form.data['name']
            slug = form.data['slug']
            descripton = form.data['descripton']
            publish_from = form.data['publish_from']
            publish_to = form.data['publish_to']

            page_structure = PageStructure.objects.create()

            page = Page(
                name=name,
                slug=slug,
                descripton=descripton,
                publish_from=datetime.strptime(publish_from, '%Y-%m-%dT%H:%M'),
                publish_to=datetime.strptime(publish_to, '%Y-%m-%dT%H:%M'),
                page_structure=page_structure,
                author=request.user,
            )
            page.save()

        return redirect("pages")