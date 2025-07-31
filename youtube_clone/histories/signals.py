from videos.signals import video_viewed

from django.utils import timezone
from histories.models import History


def create_or_update_history_record(sender, video_instance, user, **kwargs):

    if user and user.is_authenticated:
        history_record, created = History.objects.get_or_create(
            user=user,
            video=video_instance,
            defaults={'created': timezone.now()}
        )

        if not created:
            history_record.created = timezone.now()
            history_record.save()

video_viewed.connect(create_or_update_history_record)
