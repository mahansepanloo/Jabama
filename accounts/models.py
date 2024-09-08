from django.db import models
from django.contrib.auth.models import User


class Buyer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    walet = models.IntegerField(default=1000)


class Owner(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    walet = models.IntegerField(default=0)


class Suporter(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)



