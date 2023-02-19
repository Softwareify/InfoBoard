from snippets.wyswig.models import WyswigSnippet

SNIPPET_LIST_AVAILABLE_NAMES = {"wyswig_snippet": WyswigSnippet}


def get_ref_snippet_cls(ref_name_snippet):
    return SNIPPET_LIST_AVAILABLE_NAMES.get(ref_name_snippet)
