from django.contrib.auth.models import AbstractUser
from django.db import models


class University(models.Model):
	name = models.CharField(max_length=225)
	symbol_name = models.CharField(max_length=225)
	logo = models.ImageField(upload_to='university_logo')


class Team(models.Model):
	name = models.CharField(max_length=50)
	university = models.ForeignKey('University', on_delete=models.CASCADE)


class Position(models.Model):
	name = models.CharField(max_length=50)


class Account(AbstractUser):
	team = models.ForeignKey(Team, null=True, on_delete=models.CASCADE)
	position = models.ForeignKey(Position, null=True, on_delete=models.CASCADE)
	university = models.ForeignKey(University, null=True, on_delete=models.CASCADE)
