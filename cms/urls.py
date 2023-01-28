from django.contrib import admin
from django.urls import include, path

from .views import main

urlpatterns = [
    path("", main, name="cms"),
    path("admin/", admin.site.urls),
    path("auth/", include("authentication.urls")),
]
