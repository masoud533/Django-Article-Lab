from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserCreationForm(CustomUserCreationForm):

    class Meta:
        model = User
        fields = ('email',)

class CustomUserAdmin(UserAdmin):
    model = User
    add_form = CustomUserCreationForm
    list_display = ('email', "is_superuser", "is_active")
    list_filter = ('email', "is_superuser", "is_active")
    search_fields = ('email')
    ordering = ('email')
    fieldsets = (
        (None, {
            "fields": (
                'email', 'password'
            ),
        }),
        ('permissions', {
            "fields": (
                "is_staff", 'is_active', 'is_superuser'
            ),
        }),
        ('group permissions', {
            "fields": (
                "groups", 'user_permissions',
            ),
        }),
        ('important date', {
            "fields": (
                "last_login",
            ),
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password', 'is_staff', 'i_superuser', 'is_active')
        }),
    )

admin.site.register(User,CustomUserAdmin)