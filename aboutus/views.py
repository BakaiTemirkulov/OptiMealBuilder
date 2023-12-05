from django.shortcuts import render
from .models import AboutUs

def about_us_view(request):
    about_info = AboutUs.objects.first()  # Получаем первый объект модели AboutUs

    return render(request, 'aboutus/aboutus.html', {'about_info': about_info})



