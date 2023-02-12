from datetime import datetime

from django.forms import ModelForm

from .models import Page


class PageBaseForm(ModelForm):
    class Meta:
        model = Page
        fields = "__all__"


    def clean_publish_from(self):
        publish_from_cleaned = self.cleaned_data["publish_from"]
        if not publish_from_cleaned:
            return None
        return self.cleaned_data["publish_from"]

    def clean_publish_to(self):
        publish_to_cleaned = self.cleaned_data["publish_to"]
        if not publish_to_cleaned:
            return None
        return self.cleaned_data["publish_to"]


class PageAddForm(PageBaseForm):
    class Meta(PageBaseForm.Meta):
        fields = None
        exclude = (
            "status",
            "created",
            "modified",
            "page_structure",
            "author",
        )


class PageEditForm(PageBaseForm):
    class Meta(PageBaseForm.Meta):
        exclude = (
            "author",
            "created",
            "modified",
            "page_structure",
            "status",
        )
