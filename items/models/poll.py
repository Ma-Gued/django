from django.db import models
from django.contrib.auth.models import User

class Poll(models.Model):
    question = models.CharField(max_length=255)
    # votes = models.ManyToManyField('Vote', through='UserVote')  # Association avec les votes


    def __str__(self):
        return self.question