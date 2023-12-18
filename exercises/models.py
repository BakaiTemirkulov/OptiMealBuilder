from django.db import models

class ExerciseCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Exercise(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    category = models.ForeignKey(ExerciseCategory, on_delete=models.CASCADE)
    difficulty = models.CharField(max_length=50)
    image = models.ImageField(upload_to='exercise_images/', null=True, blank=True)
    video_url = models.URLField(null=True, blank=True)
    effectiveness = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name

class UserExercise(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    date_completed = models.DateField()

    # Здесь можно добавить другие поля, такие как количество повторений, вес и т. д.,
    # чтобы отслеживать прогресс пользователя

    def __str__(self):
        return f"{self.user.username} - {self.exercise.name} - {self.date_completed}"



