from datetime import datetime

from content.page.services import PageService
from publisher.models import Task


class PublicationService:
    model = Task

    @classmethod
    def add_task(cls, *, type_publication: str, object_id: int, due_date: datetime):
        defaults = {"type_publication": type_publication, "object_id": object_id, "due_date": due_date, "execution_date": None}
        return cls.model.objects.filter(
            type_publication=type_publication, object_id=object_id, due_date=due_date
        ).update_or_create(defaults=defaults)

    @staticmethod
    def page_publish(page_id: int):
        return PageService.publish(page_id=page_id)
