from django.db import transaction

from content.page_structure.models import PageStructure
from snippets.services import SnippetService


class PageStructureService:
    @staticmethod
    @transaction.atomic
    def update_structure(*, page_structure: PageStructure, updated_data: dict):
        snippets_data = SnippetService.get_snippets_info(data=updated_data)
        for snippet_data in snippets_data:
            if snippet_data["snippet_ref_name"]:
                if snippet_data["snippet_id"]:
                    pass
                else:
                    return SnippetService.update_snippet(
                        snippet=getattr(
                            page_structure, snippet_data["snippet_location"]
                        ),
                        snippet_ref_name=snippet_data["snippet_ref_name"],
                        snippet_id=None,
                    )
