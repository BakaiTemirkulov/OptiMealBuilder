from django.shortcuts import render

def mainpage(request):
    return render(request, 'mainpage/mainpage.html')

def about(request):
    return render(request, 'mainpage/about.html')

