from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import NewUserForm
from .models import UserAcc, packages, notes, dataset

# Register your models here.

class AdminUserAcc(UserAdmin):
    add_form = NewUserForm
    model = UserAcc

    list_display = ('email','firstname','lastname','credit','is_active')
    list_filter = ('email','firstname','lastname','credit')

    fieldsets = (
        (None, {'fields': ('email', 'password','credit')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)



admin.site.register(UserAcc, AdminUserAcc)
admin.site.register(notes)
admin.site.register(dataset)