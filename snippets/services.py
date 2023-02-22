from django.db import transaction

from snippets.models import Snippet

from .utils import get_ref_snippet_cls


class SnippetService:
    @staticmethod
    @transaction.atomic
    def update_snippet(
        *, snippet: Snippet, snippet_ref_name: str, snippet_id: int | None
    ) -> Snippet.ref_snippet_obj:
        if not (snippet.snippet_id and snippet_id):
            ref_snippet = get_ref_snippet_cls(snippet_ref_name).objects.create()
            snippet.snippet_id = ref_snippet.id
            snippet.type = snippet_ref_name
            snippet.save()

            return ref_snippet

    @staticmethod
    def get_snippets_info(*, data: dict):
        snippets_info = list()
        for snippet_location, snippet_ref_name in data.items():
            if snippet_location.endswith("snippet"):
                if len(snippet_ref_name.split("-")) > 1:
                    snippet_ref_name, snippet_id = snippet_ref_name.split("-")
                    snippets_info.append(
                        {
                            "snippet_location": snippet_location,
                            "snippet_ref_name": snippet_ref_name,
                            "snippet_id": snippet_id,
                        }
                    )
                else:
                    snippets_info.append(
                        {
                            "snippet_location": snippet_location,
                            "snippet_ref_name": eval(snippet_ref_name)
                            if snippet_ref_name == "None"
                            else snippet_ref_name,
                            "snippet_id": None,
                        }
                    )

        return snippets_info
