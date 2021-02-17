from datetime import timedelta

from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


class Poll(models.Model):
    title = models.CharField(max_length=255)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(default=timezone.now().date() + timedelta(days=1))
    description = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'poll'


class Question(models.Model):
    poll = models.ForeignKey(to=Poll, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()

    QUESTION_TYPES = (
        ('text', 'Текстовый ответ'),
        ('one', 'Один ответ'),
        ('multiple', 'Несколько ответов')
    )

    type = models.CharField(max_length=50, choices=QUESTION_TYPES)

    def __str__(self):
        return self.text

    class Meta:
        db_table = 'question'


class Choice(models.Model):
    text = models.TextField()
    question = models.ForeignKey(to=Question, on_delete=models.CASCADE, related_name='choices', default='self')

    def __str__(self):
        return self.text

    class Meta:
        db_table = 'choice'


class Answer(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.DO_NOTHING, default='self')
    poll = models.ForeignKey(to=Poll, on_delete=models.DO_NOTHING,
                             related_name='polls', default='self')
    question = models.ForeignKey(to=Question, on_delete=models.DO_NOTHING,
                                 related_name='questions', default='self')
    choice = models.ForeignKey(to=Choice, on_delete=models.DO_NOTHING, null=True,
                               related_name='choice', default='self')
    text_vote = models.TextField()

    class Meta:
        db_table = 'answer'
