from django.db import models
from django.contrib.auth.models import User
from .vote import Vote

class UserVote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vote = models.ForeignKey(Vote, on_delete=models.CASCADE)
    
