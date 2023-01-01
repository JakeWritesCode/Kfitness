import django.db.models
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Exercise(models.Model):
    """
    A model that stores user defined exercises along with
    storing of user weight, rep and set values

    """
    name = models.CharField(max_length=500)
    description = models.TextField()
    weight = models.FloatField()
    sets = models.IntegerField()
    reps = models.IntegerField()
    def __str__(self):
        return f"{self.name} - total weight lifted: {self.total_weight_lifted()}"

    def total_weight_lifted(self):
        return self.weight*(self.sets*self.reps)
