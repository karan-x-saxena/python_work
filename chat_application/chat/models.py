from pyexpat import model
from tabnanny import check
from django.db import models
from datetime import datetime

class Space(models.Model):
    name = models.CharField(max_length=1000)

class Message(models.Model):
    value = models.CharField(max_length=1000000000000)
    date = models.DateField(default=datetime.now,blank=True)
    user = models.CharField(max_length=100000000000)
    room = models.CharField(max_length=100000000)

class room(models.Model):
    username = models.CharField(max_length=100)
    room = models.CharField(max_length=50)

class Permission(models.Model):
    superuser = models.CharField(max_length=100)
    space = models.CharField(max_length=50)
    user = models.CharField(max_length=50)
    check_user = models.BooleanField(default=False)

class SpaceX(models.Model):
    name = models.CharField(max_length=1000)
    user = models.CharField(max_length=100)
# Create your models here.
