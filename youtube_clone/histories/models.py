from django.conf import settings
from django.db import models

# Create your models here.
class History(models.Model):
     video = models.ForeignKey(
          "videos.Video",
          on_delete=models.CASCADE,
          related_name='video_history_records',
          verbose_name='Video Viewed',
     )
     user = models.ForeignKey(
          settings.AUTH_USER_MODEL,
          on_delete=models.CASCADE,
          related_name='user_history_records',
          verbose_name='Viewed By',
     )
     created = models.DateTimeField(auto_now_add=True)

     class Meta:
        unique_together = ('user', 'video')

        verbose_name = "View History Record"
        verbose_name_plural = "View History Records"
        ordering = ['-created']
