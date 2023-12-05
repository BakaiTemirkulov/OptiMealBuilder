from django.urls import path
from . import views
from .views import food_list


urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('products/', food_list, name='products_list'),
]

