from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class register(models.Model):
    """
    A model that stores user defined exercises along with
    storing of user weight, rep and set values

    """
    first_name = models.CharField(max_length=500)
    second_name = models.CharField(max_length=500)
    email_address = models.CharField(max_length=500)
    email_address = models.CharField(max_length=500)
    def __str__(self):
        return f"{self.name} - total weight lifted: {self.total_weight_lifted()}"

    def total_weight_lifted(self):
        return self.weight*(self.sets*self.reps)