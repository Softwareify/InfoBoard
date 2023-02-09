from django.contrib.auth import get_user_model
from django.db import transaction

from ..page_structure.models import PageStructure
from .models import Page

User = get_user_model()


class PageService:
    @staticmethod
    @transaction.atomic
    def create_page(*, page_data: dict, user: User):
        page_structure = PageStructure.objects.create()
        page_data.update({"page_structure": page_structure})
        page = Page.objects.create(**page_data, author=user)

        return page
