from django.db import models
from users.models import User


class Comment(models.Model):

    user = models.ForeignKey(
       User,
    )

    content = models.TextField()
