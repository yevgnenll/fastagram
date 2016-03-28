from django.db import models

from users.models import User


class Post(models.Model):

    content = models.TextField()

    image = models.ImageField(
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    user = models.ForeignKey(
        User,
    )
