from django.contrib import admin

from .models import Carousels, Content, Groups, Posts, TelegramUsers


@admin.register(Groups)
class GroupAdmin(admin.ModelAdmin):
    list_display = ["group_id", "group_name", "group_vk_id", "created_at"]
    list_display_links = ("group_name",)
    list_filter = (
        "created_at",
        "group_name",
        "group_id",
    )


@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    list_display = [
        "post_id",
        "text",
        "url",
    ]
    list_filter = ("post_id",)


@admin.register(TelegramUsers)
class TelegramUsersAdmin(admin.ModelAdmin):
    list_display = [
        "telegram_id",
        "username",
        "first_name",
        "last_name",
        "registered_at",
    ]

    list_display_links = ("username",)
    list_filter = (
        "telegram_id",
        "username",
        "first_name",
        "last_name",
        "registered_at",
    )


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = [
        "content_id",
        "content_vk_id",
        "public_date",
        "save_date",
    ]
    list_filter = (
        "public_date",
        "save_date",
        "content_id",
    )


@admin.register(Carousels)
class CarouselAdmin(admin.ModelAdmin):
    list_display = [
        "carousel_id",
        "text",
        "url",
        "url1",
        "url2",
        "url3",
        "url4",
        "url5",
        "url6",
        "url7",
        "url8",
        "url9",
    ]
