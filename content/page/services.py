from django.contrib.auth import get_user_model
from django.db import transaction

from snippets.models import BaseSnippet

from ..page_structure.models import PageStructure
from .models import Page

User = get_user_model()


class PageService:
    @staticmethod
    @transaction.atomic
    def create_page(*, page_data: dict, user: User):
        page_structure = PageStructure.objects.create()
        page_structure.header_snippet = BaseSnippet.objects.create()
        page_structure.content_snippet = BaseSnippet.objects.create()
        page_structure.footer_snippet = BaseSnippet.objects.create()
        page_structure.save()
        page_data.update({"page_structure": page_structure})
        page = Page.objects.create(**page_data, author=user)
        return page

    @staticmethod
    @transaction.atomic
    def update_page(*, page: Page, page_new_data: dict, user: User):
        for key, value in page_new_data.items():
            setattr(page, key, value)
        page.author = user
        page.save()
