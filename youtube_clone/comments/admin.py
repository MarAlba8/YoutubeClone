from django.contrib import admin

from comments.models import Comment
from videos.models import Video


# Register your models here.
@admin.register(Comment)
class CommentsAdmin(admin.ModelAdmin):
     model = Video
