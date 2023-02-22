from django.db import transaction


class WyswigSnippetService:
    @staticmethod
    @transaction.atomic
    def update():
        pass

    @staticmethod
    @transaction.atomic
    def create():
        pass
