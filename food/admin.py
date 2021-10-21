from django.contrib import admin
from .models import  foodModels, Category


@admin.action(description="Make publishde all selected items")
def make_pub(modeladmin, request, queryset):
    row_up = queryset.update(check=True)
    if row_up == 1:
        massage = "منتشر شد"
    else:
        massage = 'منتشر شدند'
    modeladmin.message_user(request, "{} Maghale {}".format(row_up, massage))
@admin.register(foodModels)
class adminFoodModels(admin.ModelAdmin):
    list_display = ('name', 'rate','user', 'check','special_article', 'categ_to_str')
    search_fields = ('desc', 'name')
    prepopulated_fields = {'slug':('name',)}
    list_filter = ('check',)
    actions = [make_pub,]


@admin.register(Category)
class categoryAdmin(admin.ModelAdmin):
    list_display = ('name','parent')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['-parent']
# Register your models here.
