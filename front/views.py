from django.shortcuts import render

from content.page.models import Page


# Create your views here.
def main(request, slug=""):
    page = Page.objects.get(slug=slug)
    return render(request, "front/base.html", {"page": page})
