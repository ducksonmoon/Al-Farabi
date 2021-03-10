from django.db import models
from django.contrib.auth.models import AbstractUser


class Position(models.Model):
	name = models.CharField(max_length=50)


class Team(models.Model):
	name = models.ForeignKey(Position, on_delete=models.CASCADE)


class Account(AbstractUser):
	team = models.ForeignKey(Team, null=True, on_delete=models.CASCADE)
