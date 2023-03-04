from django.urls import include, path

from content.page.views import PageCMSAddView, PageCMSEditView
from content.page_structure.views import PageStructreEditView

urlpatterns = [
    path("", PageCMSAddView.as_view(), name="pages"),
    path("pages/<int:pk>/edit", PageCMSEditView.as_view(), name="page"),
    path(
        "pages/<int:pk>/edit-structure",
        PageStructreEditView.as_view(),
        name="page-structure",
    ),
    path(
        "pages/<int:pk>/edit-structure/<int:pk_structure>",
        PageStructreEditView.as_view(),
        name="page-structure",
    ),
    path("auth/", include("authentication.urls")),
]
