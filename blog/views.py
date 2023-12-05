from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Food, Consume
from django.contrib.auth.decorators import login_required


@login_required
def calorie_tracker(request):
    user = request.user
    consumed_foods = Consume.objects.filter(user=user)

    total_carbs = total_protein = total_fats = total_calories = 0

    for consumed_food in consumed_foods:
        food = consumed_food.food_consumed
        total_carbs += food.carbs
        total_protein += food.protein
        total_fats += food.fats
        total_calories += food.calories

    cal_per = (total_calories / 2000) * 100

    context = {
        'consumed_foods': consumed_foods,
        'totalCarbs': total_carbs,
        'totalProtien': total_protein,
        'totalFats': total_fats,
        'totalCalories': total_calories,
        'calPer': cal_per,
    }

    return render(request, 'post.html', context)



def hello(request):
    return HttpResponse('<h1>Hello World</h1>')

def index(request):

    if request.method == "POST":
        food_consumed = request.POST['food_consumed']
        consume = Food.objects.get(name=food_consumed)
        user = request.user
        consume = Consume(user=user, food_consumed=consume)
        consume.save()
        foods = Food.objects.all()

    else:
        foods = Food.objects.all()
    consumed_food = Consume.objects.filter(user=request.user)

    return render(request, 'post.html', {'foods': foods, 'consumed_food': consumed_food})

def delete_consume(request, id):
    consumed_food = Consume.objects.get(id=id)
    if request.method == 'POST':
        consumed_food.delete()
        return redirect('/tracker/')
    return render(request, 'delete.html')

def food_list(request):
    food = Food.objects.all()
    return render(request, 'products_list.html', {'food': food})

def aboutus(request):
    about_info = AboutUs.objects.first()
    return render(request, 'about_us_template.html', {'about_info': about_info})







