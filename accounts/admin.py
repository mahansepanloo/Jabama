from django.contrib import admin
from accounts.models import Owner,Buyer

@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    pass


@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    pass