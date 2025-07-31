from django import forms

from videos.models import Video


class CreateVideoForm(forms.ModelForm):
     title = forms.CharField(
          widget=forms.TextInput(
               attrs={'placeholder': 'Video Title'}
     ))

     embed_url = forms.CharField(
          widget=forms.TextInput(
               attrs={'placeholder': 'Embed Link'}
     ))

     class Meta:
          model = Video
          fields = ['title', 'embed_url']
