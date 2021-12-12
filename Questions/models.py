from django.db import models

# Create your models here.


class Question(models.Model):
    id = models.AutoField(primary_key=True)
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
