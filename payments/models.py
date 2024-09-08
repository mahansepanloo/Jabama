from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id}"


class Usr(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self) -> str:
        return self.email


class Copun(models.Model):
    code = models.CharField(max_length=15, unique=True)
    percent = models.IntegerField()
    expire_date = models.DateField()
    users = models.ManyToManyField(User, related_name='coupons')

    def __str__(self) -> str:
        return self.code


class Factor(models.Model):
    date = models.DateField()
    order = models.ForeignKey(Order, on_delete=models.PROTECT, related_name='factors')
    status = models.BooleanField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    copun = models.ForeignKey(Copun, on_delete=models.CASCADE, related_name='factors')
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='factors')

    def __str__(self) -> str:
        return f"Factor {self.id} - {self.order}"


class Transaction(models.Model):
    dargah = models.CharField(max_length=20)
    trans_id = models.CharField(max_length=20, unique=True)
    copun = models.ForeignKey(Copun, on_delete=models.CASCADE, related_name='transactions')
    factor = models.ForeignKey(Factor, on_delete=models.PROTECT, related_name='transactions')
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='transactions')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Transaction {self.trans_id} - {self.dargah}"
