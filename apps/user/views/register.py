from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.views import View

from apps.user.forms import RegisterForm, LoginForm
from apps.user.dto.register import RegisterEmailRequestDTO
from apps.user.repositories.user import UserRepository
from apps.user.services.user import UserService


class RegisterView(View):
    service: UserService
    template_name: str = "core/login.html"

    def setup(self, request: HttpRequest, *args: object, **kwargs: object) -> None:
        super().setup(request, *args, **kwargs)
        user_repo = UserRepository()
        self.service = UserService(user_repository=user_repo)

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(
            request,
            self.template_name,
            {
                "login_form": LoginForm(),
                "register_form": RegisterForm(),
                "active_tab": "register",
            },
        )

    def post(self, request: HttpRequest) -> HttpResponse:
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            if self.service.is_user_exists(register_form.cleaned_data["email"]):
                register_form.add_error("email", "Email already exists")
                return render(
                    request,
                    self.template_name,
                    {
                        "login_form": LoginForm(),
                        "register_form": register_form,
                        "active_tab": "register",
                    },
                )
            dto = RegisterEmailRequestDTO(
                username=register_form.cleaned_data["username"],
                email=register_form.cleaned_data["email"],
                first_name=register_form.cleaned_data["first_name"],
                last_name=register_form.cleaned_data["last_name"],
                password=register_form.cleaned_data["password"],
            )
            user = self.service.create_user(dto)
            login(request, user)
            return redirect("dashboard")

        return render(
            request,
            self.template_name,
            {
                "login_form": LoginForm(),
                "register_form": register_form,
                "active_tab": "register",
            },
        )
