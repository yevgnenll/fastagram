from django.contrib import admin

from posts.models import Post


@admin.register(Post)
class PostAdminModel(admin.ModelAdmin):

    list_display = admin.ModelAdmin.list_display + (

        'content',
        'user',
        'image',
        'created_at',
        'updated_at',
    )

    list_filter = (
        'created_at',
        'updated_at',
    )

    search_field = (
        'content'
        'user',
    )
