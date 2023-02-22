from snippets.wyswig.forms import WyswigSnippetForm
from snippets.wyswig.models import WyswigSnippet

SNIPPET_LIST_AVAILABLE_NAMES = {"wyswig_snippet": WyswigSnippet}
SNIPPET_LIST_AVAILABLE_FORMS = {"wyswig_snippet": WyswigSnippetForm}


def get_ref_snippet_cls(ref_name_snippet):
    return SNIPPET_LIST_AVAILABLE_NAMES.get(ref_name_snippet)


def get_ref_snippet_cls_form(ref_name_snippet):
    return SNIPPET_LIST_AVAILABLE_FORMS.get(ref_name_snippet)
