from django.urls import path

from modules.video.views import VideoModuleCMSAddView, VideoModuleCMSEditView

urlpatterns = [
    path("videos", VideoModuleCMSAddView.as_view(), name="videos"),
    path("videos/<int:pk>/edit", VideoModuleCMSEditView.as_view(), name="video-edit"),
]
