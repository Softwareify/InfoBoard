from django.urls import path

from modules.video.views import VideoModuleCMSAddView

urlpatterns = [path("videos", VideoModuleCMSAddView.as_view(), name="videos")]
