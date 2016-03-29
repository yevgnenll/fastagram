from posts.models import Comment, Post

from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


class AddCommentView(LoginRequiredMixin, CreateView):

    model = Comment
    fields = [
        'content',
    ]

    def form_valid(self, form):

        form.instance.user = self.request.user
        form.instance.post = Post.objects.get(
            pk=self.kwargs.get('pk')
        )
        return super(AddCommentView, self).form_valid(form)
