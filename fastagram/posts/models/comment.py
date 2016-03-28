from django.db import models

from users.models import User


class Comment(models.Model):

    user = models.ForeignKey(
        User,
    )

    post = models.ForeignKey(
        "posts.Post",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )
