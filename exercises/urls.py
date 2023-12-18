# exercises/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.exercise_list, name='exercise_list'),
    path('exercise/<int:exercise_id>/', views.exercise_detail, name='exercise_detail'),
    path('category/<int:category_id>/', views.category_exercises, name='category_exercises'),
    # Дополнительные пути URL для других представлений, если необходимо
]
