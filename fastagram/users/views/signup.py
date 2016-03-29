from django.contrib.auth import login, authenticate, get_user_model
from django.views.generic import View

from django.shortcuts import redirect, render
from django.core.urlresolvers import reverse

from users.models import User


class AuthSignupView(View):

    def get(self, request):

        return render(
            request,
            "users/signup.html",
            {}
         )

    def post(self, request):

        username = request.POST.get('username')
        password = request.POST.get('password')
        description = request.POST.get('description')

        user = User.objects.create_user(
            username=username,
            password=password,
        )

        if description:
            user.description = description
            user.save()

        login(request, authenticate(
            username=username,
            password=password,
            )
        )

        return redirect(reverse("home"))
