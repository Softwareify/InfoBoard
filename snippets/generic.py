from django.db import transaction


class GenericSnippetService:
    @staticmethod
    @transaction.atomic
    def delete_snippet(snippet_obj):
        snippet_obj.delete()
