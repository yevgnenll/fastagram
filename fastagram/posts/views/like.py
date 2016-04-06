from django.views.generic import View
from django.views.decorators.http import require_POST
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import redirect
from django.core.urlresolvers import reverse

from posts.models import Like, Post


@method_decorator(require_POST, name="dispatch")
class PostLikeView(LoginRequiredMixin, View):

    def post(self, request, slug):

        user = request.user
        post = Post.objects.get(hash_id=slug)

        like, is_created = Like.objects.get_or_create(
            user=user,
            post=post,
        )

        if not is_created:
            like.delete()

        return redirect(post)
