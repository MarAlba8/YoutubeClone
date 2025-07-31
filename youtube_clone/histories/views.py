from django.shortcuts import render
from django.views.generic import ListView

from histories.models import History


# Create your views here.
class HistoryListView(ListView):
     model = History
     template_name = 'history.html'
     context_object_name = 'history'
