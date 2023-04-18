from custom.selectors import BaseSelector

from .models import PageStructure


class PageStructureSelector(BaseSelector):
    """Page class selector"""

    model = PageStructure
