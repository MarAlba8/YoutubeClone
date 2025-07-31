from django.contrib import admin

from videos.models import Video

# Register your models here.
@admin.register(Video)
class VideosAdmin(admin.ModelAdmin):
    model = Video
