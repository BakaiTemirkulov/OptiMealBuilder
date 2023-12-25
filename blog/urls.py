from django.urls import path
from . import views
from .views import food_list
app_name = 'foods'

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('foods/', views.food_list, name='products_list'),
    path('food/<int:id>/', views.FoodDetailView.as_view()),
    path('food/<int:id>/delete/', views.FoodDeleteView.as_view()),
    path('food/<int:id>/update/', views.FoodUpdateView.as_view()),
    path('food_create/', views.FoodCreateView.as_view()),
    path("food_search/", views.food_search, name="food_search"),
]

