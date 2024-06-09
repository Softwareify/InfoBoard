from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from healthcheck.views import HealthCheckView

# from elastic_search.page.views import PageDocumentView

urlpatterns = []

router = DefaultRouter()
# router.register(r"search-page", PageDocumentView, basename="page-search")

if settings.IS_CMS:
    urlpatterns += [
        path("", include("cms.urls")),
        path("", include("snippets.urls")),
        path("api/", include(router.urls)),
    ]

if settings.IS_FRONT:
    urlpatterns += (
        [
            path("", include("front.urls")),
        ]
        + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    )

urlpatterns += [
    path("health/health-check", HealthCheckView.as_view(), name="health-check"),
]
