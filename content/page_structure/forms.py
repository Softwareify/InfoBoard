from django.forms import ModelForm

from .models import PageStructure


class PageStructureEditAddForm(ModelForm):
    class Meta:
        model = PageStructure
        fields = "__all__"
