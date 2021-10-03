from django.contrib import admin
from .models import  foodModels, Category

admin.site.disable_action('delete_selected')
# admin actions + message user for its edits
@admin.action(description="Make publishde all selected items")
def make_pub(modeladmin, request, queryset):
    row_up = queryset.update(check=True)
    if row_up == 1:
        massage = "منتشر شد"
    else:
        massage = 'منتشر شدند'
    modeladmin.message_user(request, "{} Maghale {}".format(row_up, massage))
# end admin action

@admin.action(description="Make un-published all selected items")
def make_unp(modeladmin, request, queryset):
    queryset.update(check=False)

@admin.register(foodModels)
class adminFoodModels(admin.ModelAdmin):
    list_display = ('name','showPic' ,'rate','auth', 'check', 'categ_to_str')
    search_fields = ('desc', 'name')
    prepopulated_fields = {'slug':('name',)}
    list_filter = ('check',)
    actions = [make_pub, make_unp]

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
