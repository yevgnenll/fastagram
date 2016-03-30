from django.views.generic.edit import CreateView

from posts.models import Post


class WritePostView(CreateView):

    model = Post
    fields = [
        'content',
        'image',
    ]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(WritePostView, self).form_valid(form)
