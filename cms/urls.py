from django.contrib import admin
from django.urls import include, path

from content.page.views import PageCMSAddView, PageCMSEditView

urlpatterns = [
    path("", PageCMSAddView.as_view(), name="pages"),
    path("pages/<int:page_pk>/edit", PageCMSEditView.as_view(), name="page"),
    path("admin/", admin.site.urls),
    path("auth/", include("authentication.urls")),
]
