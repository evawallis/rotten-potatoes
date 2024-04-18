from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    favoriteColor = models.CharField(max_length=30)
    follows = models.ManyToManyField("self", blank=True)

    def __str__(self):
        return self.user.username