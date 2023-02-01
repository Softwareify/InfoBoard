from typing import Any

from django.db.models.query import QuerySet

from custom.decorators import handle_not_found


class BaseSelector:
    """Base selector class with get queryset implementation"""

    model = None

    @classmethod
    def get_queryset(cls, database: str = "default") -> QuerySet:
        """Get base queryset

        :param user: user prefetching data
        :param database: database from which the data are retrieved

        :return: page queryset
        """
        return cls.model.objects.using(database)

    @classmethod
    @handle_not_found
    def get(cls, instance_id: int, database: str = "default") -> Any:
        """Getter for one database model instance.

        :param instance_id: primary key for database model instance
        :param database: database schema

        :return: any database model instance
        """
        return cls.model.objects.using(database).get(id=instance_id)

    @classmethod
    def get_all(cls, database: str = "default") -> QuerySet:
        """Getter for all database model instance.

        :param database: database schema

        :return: database queryset
        """
        return cls.model.objects.using(database).all()
