from django.urls import path

from webapp.views import *


app_name = "webapp"

urlpatterns = [
    path('', AdvertisementListView.as_view(), name="index"),
    path('advertisement/add/', AdvertisementCreateView.as_view(), name="advertisement_add"),
    path('advertisement/<int:pk>/', AdvertisementDetailView.as_view(), name="advertisement_detail"),
    path('advertisement/<int:pk>/edit/', AdvertisementUpdateView.as_view(), name='advertisement_edit'),
    path('advertisement/<int:pk>/delete/', AdvertisementDeleteView.as_view(), name='advertisement_delete'),

    path('advertisement/<int:pk>/comment/', CommentCreateView.as_view(), name='comment_create'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
]
