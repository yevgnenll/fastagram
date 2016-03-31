from django.db.models.signals import post_save
from django.dispatch import receiver

from posts.models import Post
from tags.models import Tag

from posts.utils import find_tags


@receiver(post_save, sender=Post)
def post_save_hashid(sender, instance, created, **kwargs):

    if not instance.hash_id:
        instance.make_hash_id()


@receiver(post_save, sender=Post)
def post_save_hashtag(sender, instance, created, **kwargs):

    splited_content = find_tags(instance.content)

    for tag_name in splited_content:
        tag, is_created = Tag.objects.get_or_create(
            name=tag_name,
        )
        instance.tag_set.add(tag)
