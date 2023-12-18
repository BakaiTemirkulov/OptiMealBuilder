from django.contrib import admin
from .models import ExerciseCategory, Exercise, UserExercise

admin.site.register(ExerciseCategory)
admin.site.register(Exercise)
admin.site.register(UserExercise)