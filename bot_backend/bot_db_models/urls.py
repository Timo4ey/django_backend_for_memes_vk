from django.urls import path

from . import views


urlpatterns = [
    path('groups/', views.GroupsListView.as_view()),
    path('groups/<int:pk>/',
         views.GroupsDetailView.as_view()),

    path('content/', views.ContentListView.as_view()),
    path('content/<int:pk>/', views.ContentDetailView.as_view()),

    path('posts/', views.PostListView.as_view()),
    path('posts/<int:pk>/', views.PostDetailView.as_view()),

    path('carousel/',
         views.CarouselListView.as_view()),
    path('carousel/<int:pk>/', views.CarouselDetailView.as_view()),

    path('telegram_users/', views.TelegramUsersView.as_view()),
]
