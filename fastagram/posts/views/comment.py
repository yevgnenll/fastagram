from posts.models import Comment, Post

from django.views.generic.edit import CreateView
from django.views.decorators.http import require_POST
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator


@method_decorator(require_POST, name="dispatch")
class AddCommentView(LoginRequiredMixin, CreateView):

    model = Comment
    slug_field = 'hash_id'
    fields = [
        'content',
    ]

    def form_valid(self, form):

        form.instance.user = self.request.user
        form.instance.post = Post.objects.get(
            hash_id=self.kwargs.get('slug'),
        )
        return super(AddCommentView, self).form_valid(form)
