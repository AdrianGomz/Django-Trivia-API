from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    publication_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='questions')
    question = models.TextField(null=False)
    category = models.CharField(max_length=50)
    ansA = models.CharField(max_length=100)
    ansB = models.CharField(max_length=100)
    ansC = models.CharField(max_length=100)
    ansD = models.CharField(max_length=100)
    ANS_CHOICES = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
    )
    correct_ans = models.CharField(max_length=1, choices=ANS_CHOICES)

    def __str__(self):
        return self.question
