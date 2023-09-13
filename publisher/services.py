from datetime import datetime

from content.page.services import PageService
from publisher.models import Task


class PublicationService:
    model = Task

    @classmethod
    def add_task(cls, *, type_publication: str, object_id: int, due_date: datetime):
        return cls.model.objects.create(
            type_publication=type_publication, object_id=object_id, due_date=due_date
        )

    @staticmethod
    def page_publish(page_id: int):
        return PageService.publish(page_id=page_id)
