from django.contrib import admin
from django.urls import path, include
from blog import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("blog.urls")),
    path('tracker/', views.index, name="index"),
    path('delete/<int:id>/', views.delete_consume, name="delete"),
    path('food/', views.food_list, name="products_list"),
    path('', include('mainpage.urls')),
    path('', include('registration.urls')),
    path("food_search/", views.food_search, name="food_search"),
    path('', include('aboutus.urls')),
    path('exercises/', include('exercises.urls')),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
