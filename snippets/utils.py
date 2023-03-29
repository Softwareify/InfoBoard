from snippets.video_snippet.forms import VideoSnippetForm
from snippets.video_snippet.models import VideoSnippet
from snippets.video_snippet.services import VideoSnippetService
from snippets.wyswig.forms import WyswigSnippetForm
from snippets.wyswig.models import WyswigSnippet
from snippets.wyswig.services import WyswigSnippetService

SNIPPET_LIST_AVAILABLE_NAMES = {
    "wyswig_snippet": WyswigSnippet,
    "video_snippet": VideoSnippet,
}
SNIPPET_LIST_AVAILABLE_FORMS = {
    "wyswig_snippet": WyswigSnippetForm,
    "video_snippet": VideoSnippetForm,
}
SNIPPET_LIST_AVAILABLE_SERVICE = {
    "wyswig_snippet": WyswigSnippetService,
    "video_snippet": VideoSnippetService,
}


def get_snippet_cls(ref_name_snippet):
    return SNIPPET_LIST_AVAILABLE_NAMES.get(ref_name_snippet)


def get_snippet_form(ref_name_snippet):
    return SNIPPET_LIST_AVAILABLE_FORMS.get(ref_name_snippet)


def get_snippet_service(ref_name_snippet):
    return SNIPPET_LIST_AVAILABLE_SERVICE.get(ref_name_snippet)


def eval_none_or_get_var(string):
    if string == "None":
        return eval(string)
    return string
