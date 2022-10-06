from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Goat(models.Model):

    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    bio = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Expertise(models.Model):

    title = models.CharField(max_length=150)
    strength = models.IntegerField(default=0)
    goat = models.ForeignKey(Goat, on_delete=models.CASCADE, related_name="expertises")

    def __str__(self):
        return self.title

class CustomGoat(models.Model):

    title = models.CharField(max_length=150)
    # this is going to create the many to many relationship and join table
    expertises = models.ManyToManyField(Expertise)

    def __str__(self):
        return self.title



