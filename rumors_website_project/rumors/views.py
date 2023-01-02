from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, DetailView
from .models import Community, Post
from django.urls import reverse_lazy, reverse
from .forms import CommunityForm, PostForm
from django.contrib.auth.models import Permission




def home(request):
    return render(request, 'rumors/home.html')


def about(request):
    return render(request, 'rumors/about.html')


def JoinButton(request):
      if request.method == "POST":
        user = request.user
        model_id = request.POST['id']
        all_permissions = Permission.objects.filter(content_type__app_label='blog', content_type__model='post')
        if not user.has_perm('rumors.add_post') or not user.has_perm('rumors.delete_post'):
          permission_add = Permission.objects.get(codename="rumors.add_post")
          permission_remove = Permission.object.get(codename='rumors.delete_post')
          user.user_permissions.add(permission_add, permission_remove)
          return redirect(reverse('rumors-detail', args=model_id))
        else:
             return redirect(reverse('rumors-detail', args=model_id))
   
      

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
