from django.urls import path
from . import views

urlpatterns = [
    path('stories/', views.success_stories, name='success_stories'),
    path('stories/<int:id>/', views.StoryDetailView.as_view(), name='story_detail'),
    path('stories/<int:story_id>/comments/', views.add_comment, name='add_comment'),

]