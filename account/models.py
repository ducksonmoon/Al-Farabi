from django.db import models
from django.contrib.auth.models import AbstractUser


class Positions(models.Model):
	name = models.CharField(max_length=50)


class Team(models.Model):
	name = models.ForeignKey(Positions, on_delete=models.CASCADE)


class Account(AbstractUser):
	team = models.ForeignKey(Team, on_delete=models.CASCADE)
