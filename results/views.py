from .models import SuccessStory
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from .models import SuccessStory, CommentModel
from django.shortcuts import render, get_object_or_404, redirect
from . import models



def success_stories(request):
    stories = SuccessStory.objects.all()
    return render(request, 'success_stories.html', {'stories': stories})

class StoryDetailView(generic.DetailView):
    template_name = 'story_detail.html'

    def get_object(self, **kwargs):
        story_id = self.kwargs.get('id')
        return get_object_or_404(models.SuccessStory, id=story_id)


def add_comment(request, story_id):
    story = get_object_or_404(SuccessStory, pk=story_id)
    if request.method == 'POST':
        text = request.POST.get('comment_text')  # Получение текста комментария из формы
        user = request.user
        comment = CommentModel(choice_story=story, text_review=text, user=user)
        comment.save()
        return HttpResponseRedirect(reverse('story_detail', args=(story_id,))) # Перенаправление на страницу успеха
    return render(request, 'story_detail.html')  # Вернуть форму для добавления комментария








