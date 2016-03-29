from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse


class Comment(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    post = models.ForeignKey(
        "posts.Post",
    )

    content = models.TextField()

    def get_absolute_url(self):

        return reverse(
            'post', kwargs={
                'pk': self.post.id,
            }
        )
