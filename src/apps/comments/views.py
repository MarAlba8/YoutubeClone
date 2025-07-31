from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView
from comments.models import Comment
from comments.forms import CreateCommentForm
from videos.models import Video


# Create your views here.
class CommentCreateView(LoginRequiredMixin, CreateView):
     model = Comment
     form_class = CreateCommentForm
     template_name = 'detail_video.html'

     def dispatch(self, request, *args, **kwargs):
        # Store video_pk from URL kwargs for later use in form_valid and get_success_url
        self.video_pk = kwargs['pk']
        self.video_instance = get_object_or_404(Video, pk=self.video_pk)
        return super().dispatch(request, *args, **kwargs)

     def get_context_data(self, **kwargs):
        # Ensure the 'video' object is always available in the template context
        context = super().get_context_data(**kwargs)
        context['video'] = self.video_instance
        # Optionally, pass comments here if not already done in the detail view
        # context['comments'] = self.video_instance.comments.all().order_by('-created_at')
        return context

     def form_valid(self, form):
          form.instance.user = self.request.user
          form.instance.video = self.video_instance
          return super().form_valid(form)

     def get_success_url(self):
          return reverse('video_detail', kwargs={'pk': self.video_pk})
