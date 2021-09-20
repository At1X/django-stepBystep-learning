from django.contrib import admin
from .models import  foodModels, Category

@admin.register(foodModels)
class adminFoodModels(admin.ModelAdmin):
    list_display = ('name', 'rate','auth', 'check', 'categ_to_str')
    search_fields = ('desc', 'name')
    prepopulated_fields = {'slug':('name',)}
    list_filter = ('check',)

    # IMPORTANT
    def categ_to_str(self, obj):
        return ", ".join([Category.name for Category in obj.categ.all()])
    categ_to_str.short_description = 'Category'
    # IMPORTANT

@admin.register(Category)
class categoryAdmin(admin.ModelAdmin):
    list_display = ('name','parent')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['-parent']
# Register your models here.
