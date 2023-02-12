from django.db.models.query import QuerySet

from content.selectors import BaseSelector

from .models import Page


class PageSelector(BaseSelector):
    """Page class selector"""

    model = Page

    @staticmethod
    def list_pages(*, database: str = "default") -> QuerySet[Page]:
        return PageSelector.get_queryset(database).all()

    @staticmethod
    def get_page_by_id(*, page_pk: int, database: str = "default") -> Page:
        return PageSelector.get(page_pk, database)
