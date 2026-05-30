from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.views import View

from apps.user.forms import LoginForm


class LoginView(View):
    def __init__(self, **kwargs: object) -> None:
        super().__init__(**kwargs)
        self.template_name = "user/login.html"

    def get(self, request: HttpRequest) -> HttpResponse:
        form = LoginForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request: HttpRequest) -> HttpResponse:
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request=request,
                email=form.cleaned_data["email"],
                password=form.cleaned_data["password"],
            )
            if user:
                login(request, user)
                return redirect("dashboard")
            form.add_error(None, "Email or Password is incorrect")
        return render(request, self.template_name, {"form": form})
