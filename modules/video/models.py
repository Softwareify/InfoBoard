from uuid import uuid4

from django.db import models


class Video(models.Model):
    filepath = models.FileField(upload_to="./videos")
    name = models.CharField(max_length=250)
