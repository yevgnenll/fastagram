from django.views.generic.detail import DetailView

from tags.models import Tag


class TagPostDetailView(DetailView):

    model = Tag
    template_name = "posts/tags.html"
    slug_field = "name"
