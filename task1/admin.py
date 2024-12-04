from django.contrib import admin
from .models import *
@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('name',)
@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title',)

# admin.site.register(Game)
# Register your models here.
