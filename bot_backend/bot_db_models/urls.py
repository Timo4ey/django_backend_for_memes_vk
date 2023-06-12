from django.urls import path

from . import views

urlpatterns = [
    path("groups/", views.GroupsListView.as_view(), name="groups"),
    path(
        "groups/<int:pk>/",
        views.GroupsDetailView.as_view(),
        name="specific_group",
    ),
    path("content/", views.ContentListView.as_view(), name="content"),
    path(
        "content/<int:pk>/",
        views.ContentDetailView.as_view(),
        name="specific_content",
    ),
    path("posts/", views.PostListView.as_view(), name="posts"),
    path(
        "posts/<int:pk>/", views.PostDetailView.as_view(), name="specific_post"
    ),
    path("carousel/", views.CarouselListView.as_view(), name="carousel"),
    path(
        "carousel/<int:pk>/",
        views.CarouselDetailView.as_view(),
        name="specific_carousel",
    ),
    path(
        "telegram_users/",
        views.TelegramUsersView.as_view(),
        name="telegram_users",
    ),
]
