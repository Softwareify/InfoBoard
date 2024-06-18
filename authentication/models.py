from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=get_user_model())
def post_save(*_args, **_kwargs):
    instance = _kwargs.get("instance", {})
    if instance._state.db == "default":
        instance.save(using="public")
