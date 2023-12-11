from django.urls import path
from . import views

urlpatterns = [
    path('aboutus/', views.about_us_view, name='aboutus'),
]
