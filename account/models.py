from django.contrib.auth.models import AbstractUser
from django.db import models


class Position(models.Model):
	name = models.CharField(max_length=50)


class Team(models.Model):
	name = models.CharField(max_length=50)


class Account(AbstractUser):
	team = models.ForeignKey(Team, null=True, on_delete=models.CASCADE)
	position = models.ForeignKey(Position, null=True, on_delete=models.CASCADE)
