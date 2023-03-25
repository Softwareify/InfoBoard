from django.contrib.auth import get_user_model
from django.db import transaction

from snippets.models import BaseSnippet

from ..page_structure.models import PageStructure
from .models import Page

User = get_user_model()


class PageService:
    """Service for page"""

    model = Page

    @classmethod
    @transaction.atomic
    def create_page(cls, *, page_data: dict, user: User):
        """Creating page with page structure and base snippets

        :param page_data: Data of page in dict
        :param user: User object
        """
        page_structure = PageStructure.objects.create()
        page_structure.header_snippet = BaseSnippet.objects.create()
        page_structure.content_snippet = BaseSnippet.objects.create()
        page_structure.footer_snippet = BaseSnippet.objects.create()
        page_structure.save()
        page_data.update({"page_structure": page_structure})
        page = cls.model.objects.create(**page_data, author=user)
        return page

    @staticmethod
    @transaction.atomic
    def update_page(*, page: Page, page_new_data: dict, user: User):
        """Updating page

        :param page_new_data: Page new data in dict
        :param user: User object
        """
        for key, value in page_new_data.items():
            setattr(page, key, value)
        page.author = user
        page.save()
