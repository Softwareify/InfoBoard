from django.contrib import admin
from django.urls import include, path

from content.page.views import PageAddView, PageEditView

urlpatterns = [
    path("", PageAddView.as_view(), name="pages"),
    path("pages/<int:id>/edit", PageEditView.as_view(), name="page"),
    path("admin/", admin.site.urls),
    path("auth/", include("authentication.urls")),
]
