from django.urls import path

from webapp.views import *


app_name = "webapp"

urlpatterns = [
    path('', AdvertisementListView.as_view(), name="index"),
    # path('posts/add/', PostCreateView.as_view(), name="post_add"),
    # path('post/<int:pk>/', PostDetailView.as_view(), name="post_view"),
    # path('post/<int:pk>/update/', PostUpdateView.as_view(), name="post_update"),
    # path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="post_delete"),
    # path('post/<int:pk>/like/', LikePostView.as_view(), name="post_like"),
    # path('user/<int:pk>/follower/', FollowersView.as_view(), name="follower")
]
