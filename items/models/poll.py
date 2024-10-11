from django.db import models

class Poll(models.Model):
    QUESTION_CATEGORIES = [
        ('meal', 'Meal'),
        ('intendancy', 'Intendance'),
        ('game', 'Game'),
        ('logistic', 'Logistic'),
    ]

    question = models.CharField(max_length=255)
    category = models.CharField(max_length=20, choices=QUESTION_CATEGORIES, default='meal')

    def __str__(self):
        return self.question
