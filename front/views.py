from django.shortcuts import render

from content.page.selectors import PageSelector


def public(request, slug=""):
    page = PageSelector.get_page_by_slug(slug=slug, database="public")
    return render(request, "front/base.html", {"page": page})


def preview(request, pk):
    page = PageSelector.get(instance_id=pk)
    return render(request, "front/base.html", {"page": page})
