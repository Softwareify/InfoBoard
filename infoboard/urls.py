from django.conf import settings
from django.urls import include, path

urlpatterns = []

if settings.IS_CMS:
    urlpatterns += [path("", include("cms.urls")), path("", include("snippets.urls"))]

if settings.IS_FRONT:
    urlpatterns += [
        path("", include("front.urls")),
    ]
