from django.db import models

from users.models import User


class Like(models.Model):

    post = models.ForeignKey(
        "Post",
    )

    user = models.ForeignKey(
        User,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )
