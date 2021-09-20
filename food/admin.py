from django.contrib import admin
from .models import  foodModels

@admin.register(foodModels)
class adminFoodModels(admin.ModelAdmin):
    list_display = ('name', 'rate','auth', 'check')
    search_fields = ('desc', 'name')
    prepopulated_fields = {'slug':('name',)}
    list_filter = ('check',)
# Register your models here.
