from django.db import models
from django.contrib.auth.models import User

class SuccessStory(models.Model):

    def __str__(self):
        return self.user_name

    user_name = models.CharField(max_length=100)
    before_after_photo = models.ImageField(upload_to='success_stories')
    description = models.TextField(blank=True, null=True)
    before = models.FloatField(blank=True, null=True)
    after = models.FloatField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)

class CommentModel(models.Model):
    choice_story = models.ForeignKey(SuccessStory, on_delete=models.CASCADE,
                                    related_name='comment_object')
    text_review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.choice_story}'