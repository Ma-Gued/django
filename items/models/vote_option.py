from django.db import models

class VoteOption(models.Model):
    RESPONSE_CHOICES = [
        ('oui', 'Oui'),
        ('non', 'Non'),
    ]
    
    poll = models.ForeignKey('Poll', on_delete=models.CASCADE)
    meal = models.ForeignKey('Meal', null=True, blank=True, on_delete=models.CASCADE)
    intendance = models.ForeignKey('Intendance', null=True, blank=True, on_delete=models.CASCADE)
    game = models.ForeignKey('Game', null=True, blank=True, on_delete=models.CASCADE)

    response = models.CharField(max_length=3, choices=RESPONSE_CHOICES, default='oui')
      
    # def __str__(self):
    #     return f"{self.meal.name} - {self.poll.question}"