from ckeditor.fields import RichTextField
from django.db import models


class WyswigSnippet(models.Model):
    """Wyswig snippet model"""

    content = RichTextField(blank=True, null=True)
