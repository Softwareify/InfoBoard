from django.apps import AppConfig


class AuthenticationConfig(AppConfig):
    """
    The AuthenticationConfig inherit from AppConfig and enable use a authenticaion in settings

    :param default_auto_field: parameter create automatically a primary key
    :param name: parameter set a apps name for model
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'authentication'