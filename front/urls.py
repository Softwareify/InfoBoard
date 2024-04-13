from django.urls import include, path

from .views import preview, public

urlpatterns = [
    path("", public),
    path("<slug:slug>", public),
]
