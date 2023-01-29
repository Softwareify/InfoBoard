from django.db import models
from content.page.models import Page
from snippets.models import BaseSnippet


class PageStructure(models.Model):
    page = models.OneToOneField(Page, on_delete=models.CASCADE)
    header_snippet = models


