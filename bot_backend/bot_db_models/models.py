# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the
# desired behavior
#   * Remove `managed = True` lines if you wish to allow Django to create,
# modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field
# names.
from django.db import models


class Groups(models.Model):
    group_id = models.AutoField(primary_key=True)
    group_vk_id = models.IntegerField(unique=True, null=False)
    group_name = models.CharField(
        max_length=1000, blank=True, null=False, unique=False
    )
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)

    class Meta:
        managed = True
        db_table = "groups"

    def __str__(self) -> str:
        return f"{self.group_name}"


class Content(models.Model):
    content_id = models.AutoField(primary_key=True)
    content_vk_id = models.IntegerField(unique=True, null=False, default=1)
    group_id_fk = models.ForeignKey(
        "Groups", models.DO_NOTHING, blank=True, null=False
    )
    public_date = models.DateTimeField(blank=True, null=True)
    save_date = models.DateTimeField(blank=True, null=True, auto_now_add=True)

    class Meta:
        managed = True
        db_table = "content"

    def __str__(self) -> str:
        return f"Content: {self.content_id}"


class Posts(models.Model):
    post_id = models.AutoField(primary_key=True)
    url = models.CharField(
        max_length=1000, blank=True, null=False, unique=True
    )
    text = models.CharField(max_length=1000, blank=True, null=True)
    content_fk = models.ForeignKey(
        Content, models.DO_NOTHING, blank=True, null=False
    )

    class Meta:
        managed = True
        db_table = "posts"


class TelegramUsers(models.Model):
    user_id = models.AutoField(primary_key=True)
    telegram_id = models.IntegerField(unique=True, null=False)
    first_name = models.CharField(max_length=255, null=True, unique=False)
    last_name = models.CharField(max_length=255, null=True, unique=False)
    username = models.CharField(max_length=32)
    registered_at = models.DateField(auto_now_add=True)


class Carousels(models.Model):
    carousel_id = models.AutoField(primary_key=True)
    url = models.TextField(max_length=350, null=False, unique=True)
    url1 = models.TextField(max_length=350, null=False, unique=True)
    url2 = models.TextField(max_length=350, null=True, unique=True)
    url3 = models.TextField(
        max_length=350, unique=False, default=None, null=True
    )
    url4 = models.TextField(
        max_length=350, unique=False, default=None, null=True
    )
    url5 = models.TextField(
        max_length=350, unique=False, default=None, null=True
    )
    url6 = models.TextField(
        max_length=350, unique=False, default=None, null=True
    )
    url7 = models.TextField(
        max_length=350, unique=False, default=None, null=True
    )
    url8 = models.TextField(
        max_length=350, unique=False, default=None, null=True
    )
    url9 = models.TextField(
        max_length=350, unique=False, default=None, null=True
    )
    text = models.CharField(
        max_length=1000, blank=False, null=True, unique=False
    )
    content_fk = models.ForeignKey(
        Content, models.DO_NOTHING, blank=True, null=False
    )

    class Meta:
        managed = True
        db_table = "carousels"
