from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView

from histories.models import History


# Create your views here.
class HistoryListView(LoginRequiredMixin, ListView):
     model = History
     template_name = 'history.html'
     context_object_name = 'history'
     paginate_by = 10

     def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)
