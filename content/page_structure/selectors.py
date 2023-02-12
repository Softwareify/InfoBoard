from django.db.models.query import QuerySet

from content.selectors import BaseSelector

from .models import PageStructure
from ..page.models import Page


class PageStructureSelector(BaseSelector):
    """Page class selector"""

    model = PageStructure

    @staticmethod
    def get_page_structure_by_id(*, page_pk: int, database: str = "default") -> PageStructure:
        return PageStructureSelector.get(page_pk, database)
