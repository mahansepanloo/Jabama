from django.contrib import admin
from accounts.models import Owner,Suporter,Buyer

@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    pass

@admin.register(Suporter)
class SuporterAdmin(admin.ModelAdmin):
    pass
@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    pass