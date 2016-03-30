from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    phone_number = models.CharField(
        max_length=20,
    )

    description = models.TextField()

    follower_set = models.ManyToManyField(
        "self",
        related_name="followee_set",
        symmetrical=False,
        through="Follow",
    )

    def __str__(self):
        return self.username
