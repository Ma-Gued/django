from django.db import models
from clairmarais.models.poll import Poll


class VoteOption(models.Model):
    name = models.CharField(max_length=255, default='')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='poll_vote_options', blank=True, null=True) 
    
    def __str__(self):
        return self.name
