from datetime import datetime
from time import sleep

from django.core.management.base import BaseCommand

from infoboard import settings
from publisher.models import Task
from publisher.services import PublicationService


class Command(BaseCommand):
    service = PublicationService

    @classmethod
    def handle(cls, *args, **kwargs):
        while True:
            print("Run loop publisher.")
            now = datetime.now()
            tasks = Task.objects.filter(
                due_date__lte=now, retries__lt=settings.MAX_RETRIES, execution_date=None
            )
            for task in tasks:
                if not getattr(cls.service, task.type_publication)(task.object_id):
                    task.retries += 1
                else:
                    print(
                        f"Publication success. Task type: {task.type_publication}, object id: {task.object_id}"
                    )
                    task.execution_date = now
                task.save()
            sleep(5)
