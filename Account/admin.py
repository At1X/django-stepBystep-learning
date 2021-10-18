from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.register(User, UserAdmin)

UserAdmin.fieldsets[2][1]['fields'] = ('is_active', 'is_staff', 'is_superuser','is_author','vip_date', 'groups', 'user_permissions')
UserAdmin.list_display += ('is_special_user','is_author',)
# Register your models here.
