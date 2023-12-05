from django.db import models

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

