from django.apps import AppConfig


class AppConfigUser(AppConfig):

    name = "posts"

    def ready(self):
        from posts.signals.post_save import post_save_hashid, post_save_hashtag
