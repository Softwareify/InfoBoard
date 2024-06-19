from custom.decorators import handle_not_found
from custom.selectors import BaseSelector

from .models import Page


class PageSelector(BaseSelector):
    """Page class selector"""

    model = Page

    @classmethod
    @handle_not_found
    def get_page_by_slug(cls, *, slug: str, database="default") -> Page:
        return cls.get_queryset(database=database).get(slug=slug)
