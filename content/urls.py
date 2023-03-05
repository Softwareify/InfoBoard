from django.urls import path

from content.page.views import PageCMSEditView
from content.page_structure.views import PageStructreEditView

urlpatterns = [
    path("<int:pk>/edit", PageCMSEditView.as_view(), name="page"),
    path(
        "<int:pk>/edit-structure",
        PageStructreEditView.as_view(),
        name="page-structure",
    ),
]
