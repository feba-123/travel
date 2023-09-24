from django.db import models
from django.contrib.auth.models import AbstractUser
class Place(models.Model):
    name=models.CharField(max_length=30)
    desc=models.CharField(max_length=100)
    cover=models.ImageField(upload_to='app1/img',null=True,blank=True)
class Team(models.Model):
    name=models.CharField(max_length=30)
    about=models.CharField(max_length=80)
    image=models.ImageField(upload_to='app1/img', null=True, blank=True)
class Myuser(AbstractUser):
    place=models.CharField(max_length=20)
    phone=models.CharField(max_length=20)
