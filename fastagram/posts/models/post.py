from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse

from users.models import User
from tags.models import Tag

from posts.utils import find_tags, wrrap_link_node


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

    tag_set = models.ManyToManyField(
        Tag,
        null=True,
        blank=True,
    )

    like_user_set = models.ManyToManyField(
        User,
        related_name='like_user_set',
        through='Like',
    )

    class Meta:
        verbose_name = "포스트"
        verbose_name_plural = verbose_name

    def make_hash_id(self):

        from fastagram.utils import make_hash
        self.hash_id = make_hash(self)
        self.save()

    def get_absolute_url(self):

        # redirect detailpage where i wrote
        return reverse(
            'post', kwargs={
                'slug': self.hash_id
             }
        )
