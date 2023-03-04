from snippets.wyswig.forms import WyswigSnippetForm
from snippets.wyswig.models import WyswigSnippet
from snippets.wyswig.services import WyswigSnippetService

SNIPPET_LIST_AVAILABLE_NAMES = {"wyswig_snippet": WyswigSnippet}
SNIPPET_LIST_AVAILABLE_FORMS = {"wyswig_snippet": WyswigSnippetForm}
SNIPPET_LIST_AVAILABLE_SERVICE = {"wyswig_snippet": WyswigSnippetService}


def get_snippet_cls(ref_name_snippet):
    return SNIPPET_LIST_AVAILABLE_NAMES.get(ref_name_snippet)


def get_snippet_form(ref_name_snippet):
    return SNIPPET_LIST_AVAILABLE_FORMS.get(ref_name_snippet)


def get_snippet_service(ref_name_snippet):
    return SNIPPET_LIST_AVAILABLE_SERVICE.get(ref_name_snippet)

def eval_none_or_get_var(string):
    if string == 'None':
        return eval(string)
    return string
