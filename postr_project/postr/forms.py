from django import forms
from .models import Profile, Post, Comment

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'body',)
        exclude = ('author',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('body',)
        exclude = ('author',)
