from django.shortcuts import redirect

from content.page.views import PageCMSBaseView
from content.page_status.forms import PageCMSStatusForm
from content.page_status.services import PageCMSStatusService


class PageCMSStatusView(PageCMSBaseView):
    service = PageCMSStatusService

    def post(self, request, *args, **kwargs):
        page = self.get_page_obj_by_pk_from_request(*args, **kwargs)
        changed_page_status = request.POST.get("changed_page_status")
        if changed_page_status and page:
            form = PageCMSStatusForm(data=request.POST)
            if form.is_valid():
                self.service.changes_status_page(
                    page=page, new_status=form.cleaned_data["changed_page_status"]
                )
        return redirect(request.META["HTTP_REFERER"])
