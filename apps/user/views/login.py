from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.views import View

from apps.user.forms import LoginForm, RegisterForm


class LoginView(View):
    template_name = "core/login.html"

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, self.template_name, {
            "login_form": LoginForm(),
            "register_form": RegisterForm(),
            "active_tab": "login",
        })

    def post(self, request: HttpRequest) -> HttpResponse:
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = authenticate(
                request=request,
                email=login_form.cleaned_data["email"],
                password=login_form.cleaned_data["password"],
            )
            if user:
                login(request, user)
                return redirect("dashboard")
            login_form.add_error(None, "Email or Password is incorrect")

        return render(request, self.template_name, {
            "login_form": login_form,
            "register_form": RegisterForm(),
            "active_tab": "login",
        })
