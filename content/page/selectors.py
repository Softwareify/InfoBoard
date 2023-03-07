from content.selectors import BaseSelector

from .models import Page


class PageSelector(BaseSelector):
    """Page class selector"""

    model = Page
