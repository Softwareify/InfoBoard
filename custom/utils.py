from snippets.html.forms import HtmlSnippetForm
from snippets.html.models import HtmlSnippet
from snippets.html.service import HtmlSnippetService
from snippets.html.snippets import HtmlSnippetView
from snippets.video_snippet.forms import VideoSnippetForm
from snippets.video_snippet.models import VideoSnippet
from snippets.video_snippet.services import VideoSnippetService
from snippets.video_snippet.snippets import VideoSnippetView
from snippets.wyswig.forms import WyswigSnippetForm
from snippets.wyswig.models import WyswigSnippet
from snippets.wyswig.services import WyswigSnippetService
from snippets.wyswig.snippets import WyswigSnippetView

SNIPPETS = {
    "wyswig_snippet": WyswigSnippet,
    "video_snippet": VideoSnippet,
    "html_snippet": HtmlSnippet,
}
SNIPPETS_FORMS = {
    "wyswig_snippet": WyswigSnippetForm,
    "video_snippet": VideoSnippetForm,
    "html_snippet": HtmlSnippetForm,
}
SNIPPETS_SERVICES = {
    "wyswig_snippet": WyswigSnippetService,
    "video_snippet": VideoSnippetService,
    "html_snippet": HtmlSnippetService,
}
SNIPPETS_VIEWS = {
    WyswigSnippet: WyswigSnippetView,
    VideoSnippet: VideoSnippetView,
    HtmlSnippet: HtmlSnippetView,
}


def get_snippet_cls(ref_name_snippet):
    return SNIPPETS.get(ref_name_snippet)


def get_snippet_form(ref_name_snippet):
    return SNIPPETS_FORMS.get(ref_name_snippet)


def get_snippet_service(ref_name_snippet):
    return SNIPPETS_SERVICES.get(ref_name_snippet)


def get_snippet_view(obj):
    view_class = SNIPPETS_VIEWS.get(obj.__class__)
    if view_class:
        return view_class(obj)
    return None


def eval_none_or_get_var(string):
    if string == "None":
        return eval(string)
    return string
