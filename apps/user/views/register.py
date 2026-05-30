from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.views import View

from apps.user.forms import RegisterForm
from apps.user.dto.register import RegisterEmailRequestDTO
from apps.user.repositories.user import UserRepository
from apps.user.services.user import UserService


class RegisterView(View):
    def __init__(self, **kwargs: object) -> None:
        super().__init__(**kwargs)
        self.service = UserService(UserRepository())
        self.template = "user/register.html"

    def get(self, request: HttpRequest) -> HttpResponse:
        form = RegisterForm()
        return render(request, self.template, {"form": form})

    def post(self, request: HttpRequest) -> HttpResponse | HttpResponseRedirect:
        form = RegisterForm(request.POST)
        if form.is_valid():
            if self.service.is_user_exists(form.cleaned_data["email"]):
                form.add_error("email", "Email already exists")
                return render(request, self.template, {"form": form})
            dto: RegisterEmailRequestDTO = {
                "username": form.cleaned_data["username"],
                "email": form.cleaned_data["email"],
                "first_name": form.cleaned_data["first_name"],
                "last_name": form.cleaned_data["last_name"],
                "password": form.cleaned_data["password"],
            }
            user = self.service.create_user(dto)
            login(request, user)
            return redirect("dashboard")

        return render(request, self.template, {"form": form})
