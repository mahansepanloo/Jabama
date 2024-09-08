from django.contrib import admin
from .models import Ja,Rate
@admin.register(Ja)
class ModelNameAdmin(admin.ModelAdmin):
    pass

@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):
    pass