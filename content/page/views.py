import datetime

from django.http import HttpResponseNotFound
from django.shortcuts import redirect, render

from cms.views import CMSTopNavView, CMSView

from ..page_status.services import PageCMSStatusService
from .forms import PageAddForm, PageEditForm
from .selectors import PageSelector
from .services import PageService


class PageCMSBaseView(CMSView):
    """Base Page view in CMS"""

    def get(self, request, *args, **kwargs):
        self.clear_context(["videos"])
        super().get(request, *args, **kwargs)
        pages = PageSelector.get_all()
        context = {"pages": pages}
        self.add_context(context)
        return render(request, self.get_template_to_render(), self.get_context())

    def get_page_obj_by_pk_from_request(self, *args, **kwargs):
        page_id = self.kwargs.get("pk")
        if not page_id:
            return HttpResponseNotFound()
        return PageSelector.get(page_id)


class PageCMSAddView(PageCMSBaseView):
    template_name_form = "page/page_add_form.html"
    form_class = PageAddForm

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        publish_from_datetime_now = datetime.datetime.now()
        self.add_context(
            {"publish_from_datetime_now": publish_from_datetime_now.isoformat()[:-10]}
        )
        self.clear_context(["active_page"])
        return render(request, self.get_template_to_render(), self.get_context())

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        page_data = {}
        if form.is_valid():
            cleaned_data = form.clean()
            page_data.update(
                {
                    "name": cleaned_data["name"],
                    "slug": cleaned_data["slug"],
                    "description": cleaned_data["description"],
                    "publish_from": cleaned_data["publish_from"],
                    "publish_to": cleaned_data["publish_to"],
                }
            )
            PageService.create_page(page_data=page_data, user=request.user)

        self.add_context({"errors": form.errors})
        return redirect("pages")


class PageCMSBaseEditView(PageCMSBaseView, CMSTopNavView):
    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        page = self.get_page_obj_by_pk_from_request(request, *args, **kwargs)
        page_status = page.StatusChoices(page.status)
        available_statuses = PageCMSStatusService.get_available_status_page(page=page)
        self.add_context(
            {
                "page": page,
                "page_status": page_status,
                "available_statuses": available_statuses,
                "active_page": page.id,
            }
        )


class PageCMSEditView(PageCMSBaseEditView):
    template_name_form = "page/edit_page_form.html"
    form_class = PageEditForm

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        return render(request, self.get_template_to_render(), self.get_context())

    def post(self, request, *args, **kwargs):
        page = self.get_page_obj_by_pk_from_request(request, *args, **kwargs)
        form = self.form_class(data=request.POST, instance=page)
        page_new_data = {}
        if form.is_valid():
            cleaned_data = form.clean()
            page_new_data.update(
                {
                    "name": cleaned_data["name"],
                    "slug": cleaned_data["slug"],
                    "description": cleaned_data["description"],
                    "publish_from": cleaned_data["publish_from"],
                    "publish_to": cleaned_data["publish_to"],
                }
            )
            PageService.update_page(
                page=page, page_new_data=page_new_data, user=request.user
            )

        self.add_context({"errors": form.errors})
        return redirect("page", *args, **kwargs)
