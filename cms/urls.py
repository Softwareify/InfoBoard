from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

from content.page.views import PageCMSAddView
from front.views import preview

urlpatterns = [
    path("", PageCMSAddView.as_view(), name="pages"),
    path("preview/<int:pk>", preview),
    path("auth/", include("authentication.urls")),
    path("pages/", include("content.urls")),
    path("modules/", include("modules.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
