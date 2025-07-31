from django.conf import settings
from django.db import models

# Create your models here.
class Comment(models.Model):
     text = models.CharField(max_length=5000, null=False)
     video = models.ForeignKey(
          "videos.Video",
          on_delete=models.CASCADE,
          related_name='comments',
          verbose_name='Video',
     )
     user = models.ForeignKey(
          settings.AUTH_USER_MODEL,
          on_delete=models.CASCADE,
          related_name='commented_videos',
          verbose_name='Write by',
     )
