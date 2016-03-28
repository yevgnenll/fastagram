from django.db import models
from django.conf import settings

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
        settings.AUTH_USER_MODEL,
    )

    hash_id = models.CharField(
        max_length=8,
        null=True,
        blank=True,
        unique=True,
    )

    def make_hash_id(self):

        from fastagram.utils import make_hash
        self.hash_id = make_hash(self)
        self.save()
