from django.conf import settings
from django.db import models

# Create your models here.
class Reaction(models.Model):
     positive = models.BooleanField(null=False)
     video = models.ForeignKey(
          "videos.Video",
          on_delete=models.CASCADE,
          related_name='reactions',
          verbose_name='Video',
     )
     user = models.ForeignKey(
          settings.AUTH_USER_MODEL,
          on_delete=models.CASCADE,
          related_name='reacted_videos',
          verbose_name='User',
     )
