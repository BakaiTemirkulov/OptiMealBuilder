from django.urls import path
from . import views

urlpatterns = [
    path('mainpage/', views.mainpage, name='mainpage'),
    path('about/', views.mainpage, name='about'),
]
