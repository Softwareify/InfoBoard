from django.contrib.auth import get_user_model
from django.db import transaction

from content.page_status.services import PageCMSStatusService
from snippets.models import BaseSnippet
from varnish.services import VarnishService

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

    @classmethod
    @transaction.atomic
    def publish(cls, page_id: int) -> bool:
        page = Page.objects.get(id=page_id)
        PageCMSStatusService.changes_status_page(
            page=page, new_status=Page.StatusChoices.PUBLISHED.value
        )
        page.refresh_from_db()
        page.publish()
        VarnishService().purge_path(path=str(page.slug) if page.slug else "/")
        return True

    @classmethod
    @transaction.atomic
    def unpublish(cls, page_id: int) -> bool:
        page = Page.objects.get(id=page_id)
        PageCMSStatusService.changes_status_page(
            page=page, new_status=Page.StatusChoices.ARCHIVE.value
        )
        page.refresh_from_db()
        page.unpublish()
        VarnishService().purge_path(path=str(page.slug) if page.slug else "/")
        return True
