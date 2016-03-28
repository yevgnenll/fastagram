from django.contrib.auth import login
from django.views.generic import View
from django.core.urlresolvers import reverse
from django.shortcuts import render

from users.models import User


class LoginView(View):

    def get(self, request):
        context = {}

        return render(
            request,
            "users/login.html",
            context
        )

    def post(self, request):
        pass
