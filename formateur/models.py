from django.db import models

# Create your models here.
class Formateur(models.Model):
    user = models.CharField(max_length=200)
    mdp = models.CharField(max_length=40)