from rest_framework import serializers

from .models import Carousels, Content, Groups, Posts, TelegramUsers


class GroupsListSerializer(serializers.ModelSerializer):
    """List of groups"""

    class Meta:
        model = Groups
        fields = "__all__"


class ContentListSerializer(serializers.ModelSerializer):
    """List of content"""

    class Meta:
        model = Content
        fields = "__all__"


class PostListSerializer(serializers.ModelSerializer):
    """List of content"""

    class Meta:
        model = Posts
        fields = "__all__"


class CarouselListSerializer(serializers.ModelSerializer):
    """List of content"""

    class Meta:
        model = Carousels
        fields = "__all__"


class TelegramUsersListSerializer(serializers.ModelSerializer):
    """List of telegram users"""

    class Meta:
        model = TelegramUsers
        fields = "__all__"
