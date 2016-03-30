from django.db import models
from django.core.urlresolvers import reverse


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

    @property
    def tag_name(self):

        return "#{tag_name}".format(
            tag_name=self.name,
        )

    def __str__(self):
        return self.name

    def get_absolute_url(self):

        return reverse(
            'tag-detail',
            kwargs={
                'slug': self.name
            }
        )
