from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import validate_slug

class Page(models.Model):
    class StatusChoices(models.Choices):
        STATUSCHOICES = (
            (1, "Kopia robocza"),
            (2, "Do publikacji"),
            (3, "Opublikowany"),
            (4, "Do archiwum"),
            (5, "Archiwalny"),
        )

    slug = models.CharField(max_length=200, blank=False, null=False, validators=[validate_slug])
    author = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    status = models.IntegerField(choices=StatusChoices.STATUSCHOICES, max_length=1, blank=False, null=False)
    created = models.DateTimeField(auto_created=True)
    modified = models.DateTimeField(auto_created=True, auto_now=True)



