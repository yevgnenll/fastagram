from django.views.generic.list import ListView

from posts.models import Post


class PostListView(ListView):

    model = Post
    template_name = "posts/list.html"
