from django.contrib import admin

from posts.models import Comment


@admin.register(Comment)
class CommentModelAdmin(admin.ModelAdmin):

    list_display = admin.ModelAdmin.list_display + (
        'post',
        'user',
        'content',
        'created_at',
    )

    list_filter = (
        'created_at',
    )

    search_field = (
        'user',
        'post',
    )
