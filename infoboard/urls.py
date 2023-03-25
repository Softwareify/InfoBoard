from django.conf import settings
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from elastic_search.page.views import PageDocumentView

urlpatterns = []

router = DefaultRouter()
router.register(r"search-page", PageDocumentView, basename="page-search")

if settings.IS_CMS:
    urlpatterns += [
        path("", include("cms.urls")),
        path("", include("snippets.urls")),
        path("api/", include(router.urls)),
    ]

if settings.IS_FRONT:
    urlpatterns += [
        path("", include("front.urls")),
    ]
