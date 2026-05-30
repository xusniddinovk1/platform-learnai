from django.contrib.auth import logout
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.views import View


class LogoutView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        logout(request)
        return redirect("login")
