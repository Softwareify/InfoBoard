from typing import Any, Callable

from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404


def handle_not_found(function: Callable) -> Callable:
    """Decorator used to catch the 404 exception.

    :param function: Wrapped function

    :return: Wrapped function with exception catch
    """

    def inner_function(*args: Any, **kwargs: Any) -> Callable:
        try:
            return function(*args, **kwargs)
        except ObjectDoesNotExist as exception:
            raise Http404 from exception

    return inner_function
