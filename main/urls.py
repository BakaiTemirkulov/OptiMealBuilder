from django.contrib import admin
from django.urls import path, include
from blog import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("blog.urls")),
    path('tracker/', views.index, name="index"),
    path('delete/<int:id>/', views.delete_consume, name="delete"),
    path('food/', views.food_list, name="products_list"),
    path('', include('mainpage.urls')),
    path('aboutus/', views.aboutus, name='aboutus'),

]
