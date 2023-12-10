from django.db import models
from django.contrib.auth.models import User



class Food(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='blog/', blank=True)
    description = models.TextField(blank=True)
    carbs = models.FloatField()
    protein = models.FloatField()
    fats = models.FloatField()
    calories = models.IntegerField()


class Consume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food_consumed = models.ForeignKey(Food, on_delete=models.CASCADE)

class AboutUs(models.Model):
    title = models.CharField(max_length=200)
    history = models.TextField(blank=True, null=True)
    mission = models.TextField(blank=True, null=True)
    values = models.TextField(blank=True, null=True)
    team = models.TextField(blank=True, null=True)
    contact_info = models.TextField(blank=True, null=True)
    achievements = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)

    def __str__(self):
        return self.title

