from django.views.generic.edit import CreateView
from django.views.decorators.http import require_POST
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin

from tags.models import Tag
from posts.models import Post


@method_decorator(require_POST, name="dispatch")
class TagCreateView(LoginRequiredMixin, CreateView):

    model = Tag
    fields = [
        'name',
    ]
    slug_field = 'hash_id'

    def post(self, request, *args, **kwargs):

        name = request.POST.get('name')

        post = Post.objects.get(
            hash_id=kwargs.get('slug')
        )

        tag, is_created = Tag.objects.get_or_create(
            name=name
        )

        post.tag_set.add(tag)

        return redirect(post)
