from django.shortcuts import render
from django.views import View


class CMSView(View):
    template_name = "cms/side.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})


def main(request):
    return render(request, "cms/base.html")
