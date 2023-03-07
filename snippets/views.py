from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.views import View

from snippets.forms import BaseSnippetForm
from snippets.selectors import BaseSnippetSelector

from .services import BaseSnippetService
from .utils import eval_none_or_get_var, get_snippet_form


class BaseSnippetCMSView(View):
    def post(self, request, *args, **kwargs):
        with transaction.atomic():
            base_snippet = BaseSnippetSelector.get(kwargs.get("pk"))
            snippet_type = eval_none_or_get_var(request.POST.get("type"))
            if snippet_type:
                if not base_snippet.snippet:
                    snippet_form = get_snippet_form(snippet_type)(
                        instance=base_snippet.snippet, data=request.POST
                    )
                    if snippet_form.is_valid():
                        snippet = snippet_form.save()
                        BaseSnippetService.update_base_snippet(
                            base_snippet=base_snippet,
                            snippet=snippet,
                            base_snippet_type=snippet_type,
                        )

                if snippet_type == "delete_snippet":
                    BaseSnippetService.update_base_snippet_and_delete_ref_snippet(
                        base_snippet=base_snippet
                    )

                if base_snippet.snippet:
                    snippet_form = get_snippet_form(snippet_type)(
                        instance=base_snippet.snippet, data=request.POST
                    )
                    if snippet_form.is_valid():
                        snippet = snippet_form.save()

            return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
