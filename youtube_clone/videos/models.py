from django.db import models
from django.conf import settings

# Create your models here.
class Video(models.Model):
     title = models.CharField(verbose_name="Title", max_length=100, blank=False)
     embed_url = models.CharField(verbose_name="Embed URL", max_length=1000, blank=False)
     user = models.ForeignKey(
          settings.AUTH_USER_MODEL,
          on_delete=models.CASCADE,
          related_name='uploaded_videos',
          verbose_name='Created',
          null=True ##TODO: remove
     )

     def get_likes_count(self):
        return self.reactions.filter(positive=True).count()

     def get_dislikes_count(self):
        return self.reactions.filter(positive=False).count()
