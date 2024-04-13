from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.views import View

from .forms import UserLoginForm


class LoginView(View):
    """
    The LoginView object contains a query handling for login view

    :param form_class: this is a param, which initialize a user login form
    :param template_name: this is a param, which store an address to template
    """

    form_class = UserLoginForm
    template_name = "authentication/login.html"

    def get(self, request, *args, **kwargs):
        """
        Get function handling a get query for login view

        :param request: parameter storing the queries
        :param args: pass to function a variable number of parameters
        :param kwargs: pass to function a keywords(handling of dictionaries)
        :return: function return a rendered view
        """
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        """
        Post function handling a post query for login view

        :param request: parameter storing the queries
        :param args: pass to function a variable number of parameters
        :param kwargs: pass to function a keywords(handling of dictionaries)
        :return: if authentication was good, function redirect a user to cms,
         otherwise function return rendered view
        """
        form = self.form_class(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect("pages")
            else:
                return render(request, self.template_name, {"form": form})

        context = {"form": self.form_class}
        return render(request, self.template_name, context=context)


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("pages")
