from django.db import models
from django.contrib.auth.models import User


class Buyer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Owner(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    wallet = models.BigIntegerField(default=0)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.user.username




