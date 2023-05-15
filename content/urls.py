from django.urls import path

from content.page.views import PageCMSEditView
from content.page_status.views import PageCMSStatusView
from content.page_structure.views import PageCMSStructreEditView

urlpatterns = [
    path("<int:pk>/edit", PageCMSEditView.as_view(), name="page"),
    path(
        "<int:pk>/edit-structure",
        PageCMSStructreEditView.as_view(),
        name="page-structure",
    ),
    path(
        "<int:pk>/change-status", PageCMSStatusView.as_view(), name="page-change_status"
    ),
]
