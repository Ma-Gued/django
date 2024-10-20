from django.db import models
from django.contrib.auth.models import User

class ItemToBring(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        abstract = True