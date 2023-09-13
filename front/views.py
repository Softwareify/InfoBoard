from django.shortcuts import render
from django.views import View

from content.page.models import Page


def main(request, slug=""):
    page = Page.objects.using("public").get(slug=slug)
    return render(request, "front/base.html", {"page": page})
