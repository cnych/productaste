from django import forms

from apps.comment.models import Comment


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('content',)
