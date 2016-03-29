from hashids import Hashids

from posts.models import Post


def update_hash():

    posts = Post.objects.all()

    for post in posts:
        post.hash_id
        if not post.hash_id:
            post.make_hash_id()
