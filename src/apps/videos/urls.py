from django.urls import path
from videos.views import VideoCreateView, VideoDetailView, VideoListView, video_reaction_view

urlpatterns = [
    path('detail/<int:pk>/', VideoDetailView.as_view(), name='video_detail'),
    path('create', VideoCreateView.as_view(), name='video_create'),
    path('reactions/<int:pk>/react/', video_reaction_view, name='video_reaction'),
    path('', VideoListView.as_view(), name='video_list'),
]
