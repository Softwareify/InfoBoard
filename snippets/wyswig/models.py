from ckeditor.fields import RichTextField
from django.db import models
from tinymce.models import HTMLField


class WyswigSnippet(models.Model):
    """Wyswig snippet model"""

    content = HTMLField()

    def publish(self):
        self.save(using="public")
