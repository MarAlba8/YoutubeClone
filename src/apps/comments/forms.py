from django import forms

from comments.models import Comment


class CreateCommentForm(forms.ModelForm):
     text = forms.CharField(
        label="Your Comment",
        widget=forms.Textarea( attrs={'placeholder': 'Write a comment'}) # Optional: customize rows and columns
    )

     class Meta:
          model = Comment
          fields = ['text']
