from django.shortcuts import render, get_object_or_404
from .models import Exercise, ExerciseCategory

def exercise_detail(request, exercise_id):
    exercise = get_object_or_404(Exercise, pk=exercise_id)
    return render(request, 'exercises/exercise_detail.html', {'exercise': exercise})

def exercise_list(request):
    exercises = Exercise.objects.all()
    return render(request, 'exercises/exercise_list.html', {'exercises': exercises})

def category_exercises(request, category_id):
    category = get_object_or_404(ExerciseCategory, pk=category_id)
    exercises = Exercise.objects.filter(category=category)
    return render(request, 'exercises/category_exercises.html', {'category': category, 'exercises': exercises})


# Create your views here.
