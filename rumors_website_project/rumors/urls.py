from django.urls import path
from . import views
from .views import CreateCommunityView, CreatePostView, AvailableCommunitesListView, CommunitiesDetailView
urlpatterns = [
    path('', views.home, name='rumors-home'),
    path('about/', views.about, name='rumors-about'),
    path('new-community/', CreateCommunityView.as_view(),
         name='rumors-add-community'),
    path('new-post/', CreatePostView.as_view(), name='rumors-add-post'),
    path('available-communites/', AvailableCommunitesListView.as_view(),
         name='rumors-available-communites'),
    path('communites/<int:pk>/', CommunitiesDetailView.as_view(),
         name='rumors-detail'),
    path('button/', views.JoinButton,name="rumors-button")



]
