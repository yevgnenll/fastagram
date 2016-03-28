from django.contrib.auth import login, authenticate
from django.views.generic import View
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect

from users.models import User


class LoginView(View):

    def get(self, request):
        context = {}

        return render(
            request,
            "users/login.html",
            context,
        )

    def post(self, request):

        username = request.POST.get('username')
        user_pw = request.POST.get('password')

        is_user = authenticate(
           username=username,
           password=user_pw,
        )

        if is_user:
            login(request, is_user)
            return redirect(reverse("home"))

        return render(
            request,
            "home.html",
            {}
        )
