from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea

class UserAdminConfig(UserAdmin):
    search_fields = ('email', 'username', 'fname')
    list_filter = ('email', 'username', 'fname', 'is_active', 'is_staff')
    ordering = ('-start_date',)
    list_display = ('email', 'username', 'fname', 'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'username', 'fname')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'fname', 'password1', 'password2', 'is_active', 'is_staff')
        }),
    )

# Register your models here.
admin.site.register(models.NewUser, UserAdminConfig)
admin.site.register(models.Task)