from django.urls import path

from comments.views import CommentCreateView

urlpatterns = [
    path('create/<int:pk>/', CommentCreateView.as_view(), name='comment_create'),
]
