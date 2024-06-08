from django.urls import re_path

from .views import public

urlpatterns = [
    re_path(r"^(?P<slug>[a-zA-Z0-9-]*)$", public),
]
