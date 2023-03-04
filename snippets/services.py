from django.db import transaction

from snippets.models import BaseSnippet

from .utils import get_snippet_cls, get_snippet_service


class BaseSnippetService:
    @staticmethod
    @transaction.atomic
    def update_base_snippet(
        *, base_snippet: BaseSnippet, base_snippet_type: str, snippet
    ):
        base_snippet.type = base_snippet_type
        base_snippet.snippet_id = snippet.id
        return base_snippet.save()

    @staticmethod
    @transaction.atomic
    def update_base_snippet_and_delete_ref_snippet(*, base_snippet: BaseSnippet):
        base_snippet.snippet_service.delete_snippet(base_snippet.snippet)
        base_snippet.type = None
        base_snippet.snippet_id = None
        base_snippet.save()

    @staticmethod
    def get_snippets_info(*, data: dict):
        pass
