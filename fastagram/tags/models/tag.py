from django.db import models


class Tag(models.Model):

    name = models.CharField(
        max_length=20,
        unique=True
    )
    # tag has all of posting data
    # so tag must be unique field

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.name
