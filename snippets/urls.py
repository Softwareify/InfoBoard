from django.urls import path

from snippets.views import BaseSnippetCMSView

urlpatterns = [path("snippets/<int:pk>", BaseSnippetCMSView.as_view())]
