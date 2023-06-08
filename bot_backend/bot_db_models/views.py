from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.views import APIView

from bot_backend.bot_db_models.serializers import (
    CarouselListSerializer,
    ContentListSerializer,
    GroupsListSerializer,
    PostListSerializer,
    TelegramUsersListSerializer,
)
from bot_backend.bot_db_models.service import (
    has_group_id,
    has_hours_in_dict,
    upd_request_carousel,
    upd_request_data_dict,
)

from .filters import (
    get_carousels_for_specific_period,
    get_posts_for_specific_period,
)
from .models import Carousels, Content, Groups, Posts, TelegramUsers


class GroupsListView(APIView):
    """Show list of groups"""

    def get(self, request):
        groups = Groups.objects.all()
        serializer = GroupsListSerializer(groups, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=GroupsListSerializer)
    def post(self, request):
        new_data = GroupsListSerializer(data=request.data)
        if new_data.is_valid():
            new_data.save()
            return Response(status=201)
        return Response(status=400)

    @swagger_auto_schema(request_body=GroupsListSerializer)
    def put(self, request):
        instance = get_object_or_404(
            Groups, group_id=request.data.get("group_id", 0)
        )
        if not has_group_id(request.data):
            upd_request_data_dict(
                request.data, "group_vk_id", instance.group_vk_id
            )
            # request.data.update({'group_vk_id': instance.group_vk_id})
        group = GroupsListSerializer(data=request.data, instance=instance)
        if group.is_valid():
            group.save()
            return Response(status=200)
        return Response(status=400)

    @swagger_auto_schema(request_body=GroupsListSerializer)
    def delete(self, request):
        instance = get_object_or_404(Groups, group_id=request.data["group_id"])
        if instance:
            instance.delete()
            return Response(status=200)
        return Response(status=400)


class GroupsDetailView(APIView):
    """Show data of a group"""

    def get(self, request, pk):
        group = get_object_or_404(Groups, pk=pk)
        serializer = GroupsListSerializer(group)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=GroupsListSerializer)
    def put(self, request, pk):
        instance = get_object_or_404(Groups, group_id=pk)
        if not has_group_id(request.data):
            upd_request_data_dict(
                request.data, "group_vk_id", instance.group_vk_id
            )
            # request.data['group_vk_id'] = instance.group_vk_id

        group = GroupsListSerializer(data=request.data, instance=instance)
        if group.is_valid():
            group.save()
            return Response(group.data, status=200)
        return Response(status=400)

    @swagger_auto_schema(request_body=GroupsListSerializer)
    def delete(self, request, pk):
        instance = get_object_or_404(Groups, group_id=pk)
        if instance:
            instance.delete()
            return Response(status=200)
        return Response(status=400)


class ContentListView(APIView):
    """Show list of content"""

    def get(self, request):
        content = Content.objects.all()
        serializer = ContentListSerializer(content, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=ContentListSerializer)
    def post(self, request):
        instance = get_object_or_404(
            Groups, group_vk_id=request.data.get("group_id_fk", 0)
        )
        upd_request_data_dict(request.data, "group_id_fk", instance.group_id)
        # request.data.update({'group_id_fk': instance.group_id})
        new_data = ContentListSerializer(data=request.data)
        print(request.data)
        if new_data.is_valid():
            new_data.save()
            return Response(status=201)
        return Response(status=400)

    @swagger_auto_schema(request_body=ContentListSerializer)
    def put(self, request):
        instance = get_object_or_404(
            Groups, group_vk_id=request.data.get("group_id_fk", 0)
        )
        new_data = ContentListSerializer(data=request.data, instance=instance)
        if new_data.is_valid():
            new_data.save()
            return Response(status=200)
        return Response(status=400)

    @swagger_auto_schema(request_body=ContentListSerializer)
    def delete(self, request):
        instance = get_object_or_404(
            Groups, group_vk_id=request.data.get("group_id_fk", 0)
        )
        if instance:
            instance.delete()
            return Response(status=200)
        return Response(status=400)


class ContentDetailView(APIView):
    """Show data of a content"""

    def get(self, request, pk):
        content = get_object_or_404(Content, pk=pk)
        serializer = ContentListSerializer(content)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=ContentListSerializer)
    def put(self, request, pk):
        instance = get_object_or_404(Content, content_id=pk)
        content = ContentListSerializer(data=request.data, instance=instance)
        if content.is_valid():
            content.save()
            return Response(content.data, status=200)
        return Response(status=400)

    @swagger_auto_schema(request_body=ContentListSerializer)
    def delete(self, request, pk):
        instance = get_object_or_404(Content, content_id=pk)
        if instance:
            instance.delete()
            return Response(status=200)
        return Response(status=400)


class PostListView(APIView):
    """Show list of posts"""

    def get(self, request):
        if has_hours_in_dict(request.GET):
            hours = request.GET.get("hours", 1)
            posts = get_posts_for_specific_period(hours)
        else:
            posts = Posts.objects.all()
        serializer = PostListSerializer(posts, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=PostListSerializer)
    def post(self, request):
        instance = Content.objects.get(
            content_vk_id=request.data.get("content_fk")
        )
        upd_request_data_dict(request.data, "content_fk", instance.content_id)
        # request.data.update({'content_fk': instance.content_id})

        print(request.data)
        new_data = PostListSerializer(data=request.data)
        if new_data.is_valid():
            new_data.save()
            return Response(status=201)
        return Response(status=400)

    @swagger_auto_schema(request_body=PostListSerializer)
    def put(self, request):
        instance = get_object_or_404(Posts, post_id=request.data["post_id"])
        posts_upd = PostListSerializer(data=request.data, instance=instance)
        if posts_upd.is_valid():
            posts_upd.save()
            return Response(status=200)
        return Response(status=400)

    @swagger_auto_schema(request_body=PostListSerializer)
    def delete(self, request):
        print(request.data)
        group = get_object_or_404(Posts, post_id=request.data["post_id"])
        if group:
            group.delete()
            return Response(status=200)
        return Response(status=400)


class PostDetailView(APIView):
    """Show data of a posts"""

    def get(self, request, pk):
        post = get_object_or_404(Posts, pk=pk)
        serializer = PostListSerializer(post)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=PostListSerializer)
    def put(self, request, pk):
        instance = get_object_or_404(Posts, post_id=pk)
        post = PostListSerializer(data=request.data, instance=instance)
        if post.is_valid():
            post.save()
            return Response(post.data, status=200)
        return Response(status=400)

    @swagger_auto_schema(request_body=PostListSerializer)
    def delete(self, request, pk):
        instance = get_object_or_404(Posts, post_id=pk)
        if instance:
            instance.delete()
            return Response(status=200)
        return Response(status=400)


class CarouselListView(APIView):
    """Show list of posts"""

    def get(self, request):
        if has_hours_in_dict(request.GET):
            hours = request.GET.get("hours", 1)
            carousels = get_carousels_for_specific_period(hours)
        else:
            carousels = Carousels.objects.all()
        serializer = CarouselListSerializer(carousels, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=CarouselListSerializer)
    def post(self, request):
        print(request.data)
        content_id = get_object_or_404(
            Content, content_vk_id=request.data.get("content_id")
        )
        upd_request_data_dict(
            request.data, "content_id", content_id.content_id
        )

        # request.data.update({'content_id': content_id.content_id})

        new_data = CarouselListSerializer(data=request.data)
        if new_data.is_valid():
            new_data.save()
            return Response(status=201)
        return Response(status=400)

    @swagger_auto_schema(request_body=CarouselListSerializer)
    def put(self, request):
        instance = get_object_or_404(
            Content, carousel_id=request.data.get("carousel_id")
        )
        data = CarouselListSerializer(data=request.data, instance=instance)
        if data.is_valid():
            data.save
            return Response(status=200)
        return Response(status=400)

    @swagger_auto_schema(request_body=CarouselListSerializer)
    def delete(self, request):
        instance = get_object_or_404(
            Content, carousel_id=request.data.get("carousel_id")
        )
        instance.delete()
        return Response(status=200)


class CarouselDetailView(APIView):
    """Show data of a posts"""

    def get(self, request, pk):
        carousel = get_object_or_404(Carousels, pk=pk)
        serializer = CarouselListSerializer(carousel)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=CarouselListSerializer)
    def put(self, request, pk):
        instance = get_object_or_404(Carousels, carousel_id=pk)
        upd_request_carousel(request.data, instance)
        carousel = CarouselListSerializer(data=request.data, instance=instance)
        if carousel.is_valid():
            carousel.save()
            return Response(carousel.data, status=200)
        return Response(status=400)

    @swagger_auto_schema(request_body=CarouselListSerializer)
    def delete(self, request, pk):
        instance = get_object_or_404(Carousels, carousel_id=pk)
        if instance:
            instance.delete()
            return Response(status=200)
        return Response(status=400)


class TelegramUsersView(APIView):
    def get(self, request):
        user = TelegramUsers.objects.all()
        serializer = TelegramUsersListSerializer(user, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=TelegramUsersListSerializer)
    def post(self, request):
        new_data = TelegramUsersListSerializer(data=request.data)
        if new_data.is_valid():
            new_data.save()
            return Response(status=201)
        return Response(status=400)

    @swagger_auto_schema(request_body=TelegramUsersListSerializer)
    def put(self, request):
        instance = get_object_or_404(
            TelegramUsers, group_id=request.data.get("group_id", 0)
        )
        if not has_group_id(request.data):
            request.data.update({"group_vk_id": instance.group_vk_id})
        group = TelegramUsersListSerializer(
            data=request.data, instance=instance
        )
        if group.is_valid():
            group.save()
            return Response(status=200)
        return Response(status=400)

    @swagger_auto_schema(request_body=TelegramUsersListSerializer)
    def delete(self, request):
        instance = get_object_or_404(
            TelegramUsers, group_id=request.data["group_id"]
        )
        if instance:
            instance.delete()
            return Response(status=200)
        return Response(status=400)
