from django.urls import path

from webapp.moder_views import new_advertisements, approve_ad, reject_ad
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


    path('new_ads/', new_advertisements, name='new_advertisements'),
    path('approve_ad/', approve_ad, name='approve_ad'),
    path('reject_ad/', reject_ad, name='reject_ad'),

]
