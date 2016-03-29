from django.db.models.signals import post_save
from django.dispatch import receiver

from posts.models import Post


@receiver(post_save, sender=Post)
def post_save_hashid(sender, instance, created, **kwargs):

    if not instance.hash_id:
        instance.make_hash_id()
