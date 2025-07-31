import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView, DetailView, ListView

from videos.signals import video_viewed
from videos.forms import CreateVideoForm
from videos.models import Video
from reactions.models import Reaction


class VideoCreateView(CreateView):
     model = Video
     template_name = 'video/create_video.html'
     form_class = CreateVideoForm

     def form_valid(self, form):
          form.instance.user = self.request.user
          return super().form_valid(form)

     def get_success_url(self):
          return reverse('video_detail', kwargs={'pk': self.object.pk})


class VideoHomeListView(ListView):
     model = Video
     context_object_name = 'videos'
     template_name = 'home.html'

     def get_queryset(self):
        return self.model.objects.order_by('?')


class VideoListView(ListView):
     model = Video
     context_object_name = 'videos'
     template_name = 'home.html'


class VideoDetailView(DetailView):
     model = Video
     template_name = 'video/detail_video.html'

     def get_context_data(self, **kwargs):
          context = super().get_context_data(**kwargs)
          video = self.object
          video_viewed.send(
               sender=self.__class__,
               video_instance=video,
               user=self.request.user
          )
          return context


@login_required
def video_reaction_view(request, pk):
     user = request.user
     video = Video.objects.get(pk=pk)

     reaction_type = request.POST.get('reaction_type')
     reaction_positive = True if reaction_type == "like" else False

     reaction, created = Reaction.objects.get_or_create(
          user=user,
          video=video,
          defaults={'positive': reaction_positive}
     )

     if not created:
          reaction.positive = reaction_positive
          reaction.save()

     return redirect('video_detail', pk=pk)


# def most_popular_video_view(request):
#      NUMBER_MOST_POPULAR_VIDEOS = 5
#      videos = Video.objects.all().order_by('-created')

#      today = datetime.datetime.today()
#      most_popular_videos_score = []
#      most_popular_videos = []

#      for video in videos:
#           video_score = 0
#           if video.created == today:
#                video_score += 100
#           number_comments = video.comments.count()
#           number_likes = video.reactions.filter(positive=True)
#           number_dislikes = video.reactions.filter(positive=False)

#           video_score += number_comments + number_likes + number_dislikes
