from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView
from .models import Community, Post
from django.urls import reverse_lazy
from .forms import CommunityForm, PostForm


def home(request):
    return render(request, 'rumors/home.html')


def about(request):
    return render(request, 'rumors/about.html')


class AvailableCommunitesListView(ListView):
    model = Community
    template_name = 'rumors/available_communities.html'
    context_object_name = 'communities'
    ordering = ['-date_posted']




class CommunitiesDetailView(DetailView):
    model = Community
    template_name = 'rumors/communities.html'
    context_object_name = 'community'


class CreateCommunityView(CreateView):
    model = Community
    form_class = CommunityForm
    template_name = 'rumors/community_form.html'
    # make sure you know this
    success_url = reverse_lazy("rumors-home")


class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'rumors/post_form.html'
    success_url = reverse_lazy("rumors-home")
