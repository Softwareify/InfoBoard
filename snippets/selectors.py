from custom.selectors import BaseSelector
from snippets.models import BaseSnippet


class BaseSnippetSelector(BaseSelector):
    """Page class selector"""

    model = BaseSnippet
