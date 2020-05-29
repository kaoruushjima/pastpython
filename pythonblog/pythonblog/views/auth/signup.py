from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.views.generic import View


class SignupView(View):

    def get(self, request, *args, **kwargs):
        return render(
            request,
            "auth/signup.html",
            {}
        )

    def post(self, request, *args, **kwargs):
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")

        user = User.objects.create_user(
            username=username,
            password=password,
            email=email,
        )

        return redirect(reverse("auth:login"))
