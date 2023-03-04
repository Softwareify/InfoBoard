from django.db import transaction

from content.page_structure.models import PageStructure
from snippets.services import BaseSnippetService


class PageStructureService:
    @staticmethod
    @transaction.atomic
    def update_structure(*, page_structure: PageStructure, updated_data: dict):
        pass
