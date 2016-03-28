from django.db import models

from django.conf import settings


class Comment(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
    )

    post = models.ForeignKey(
        "posts.Post",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    content = models.TextField()
