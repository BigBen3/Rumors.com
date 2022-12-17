from django import forms
from .models import Community, Post


class CommunityForm(forms.ModelForm):
    class Meta:
        model = Community
        fields = ['title', 'image']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'Community']


