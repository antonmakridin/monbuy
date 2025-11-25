from django.contrib import admin
from .models import *

class MyPurchases(admin.ModelAdmin):
    list_display = ['title','cost']

admin.site.register(Purchases, MyPurchases)