from django.db import models
from django.contrib.auth.models import User
from .vote_option import VoteOption

class UserVote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vote_option = models.ForeignKey(VoteOption, on_delete=models.CASCADE)
    response = models.CharField(max_length=100)
