from django.db.models.query import QuerySet

from content.selectors import BaseSelector
from snippets.models import BaseSnippet


class BaseSnippetSelector(BaseSelector):
    """Page class selector"""

    model = BaseSnippet

    @staticmethod
    def list_base_snippets(*, database: str = "default") -> QuerySet[BaseSnippet]:
        return BaseSnippetSelector.get_queryset(database).all()

    @staticmethod
    def get_base_snippet_by_id(
        *, base_snippet_pk: int, database: str = "default"
    ) -> BaseSnippet:
        return BaseSnippetSelector.get(base_snippet_pk, database)
