from django.contrib import admin
from django.urls import include, path
from content.page.views import PageSnippetsList

urlpatterns = [
    path("", PageSnippetsList.as_view(), name="cms"),
    path("admin/", admin.site.urls),
    path("auth/", include("authentication.urls")),
]
