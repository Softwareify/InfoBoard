from django.urls import include, path

from content.page.views import PageCMSAddView

urlpatterns = [
    path("", PageCMSAddView.as_view(), name="pages"),
    path("auth/", include("authentication.urls")),
    path("pages/", include("content.urls")),
    path("modules/", include("modules.urls")),
]
