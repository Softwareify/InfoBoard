from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.views import View

from .forms import UserLoginForm, UserRegisterForm


class LoginView(View):
    form_class = UserLoginForm
    template_name = "authentication/login.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect("pages")
            else:
                return (request, self.template_name, {"form": form})

        context = {"form": self.form_class}
        return render(request, self.template_name, context=context)


class RegisterView(View):
    form_class = UserRegisterForm
    template_name = "authentication/register.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")

        context = {"form": self.form_class}
        return render(request, self.template_name, context=context)
