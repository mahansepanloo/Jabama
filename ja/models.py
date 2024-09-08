from django.db import models
from accounts.models import Owner
from django.contrib.auth.models import User


class Ja(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    addres = models.TextField()
    # img = models.ImageField()
    confirmation = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)
    update = models.DateTimeField(auto_now_add=True)

    def total_rate(self):
        total = sum([item.get_rate for item in self.jrate.all()])
        count = self.jrate.count()
        return total / count if count > 0 else 0




class Rate(models.Model):
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    ja = models.ForeignKey(Ja, on_delete=models.CASCADE, related_name="jrate")
    rate = models.IntegerField()
    created = models.DateTimeField(auto_now=True)

    def get_rate(self):
        return self.rate