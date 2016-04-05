from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdminModel(admin.ModelAdmin):

    list_display = admin.ModelAdmin.list_display + (

        'username',
        'email',

        'is_active',
        'phone_number',
        'last_login',
        'is_staff',
        'date_joined',
        'is_superuser',

    )
