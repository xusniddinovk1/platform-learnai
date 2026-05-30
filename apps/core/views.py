# apps/core/views.py
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


class LandingView(View):
    template_name = "core/index.html"

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, self.template_name)


class DashboardView(LoginRequiredMixin, View):
    template_name = "core/dashboard.html"
    login_url = "/user/login/"

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, self.template_name)
