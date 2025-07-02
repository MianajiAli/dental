from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser

    list_display = ('id', 'username', 'full_name', 'phone_number', 'role', 'is_active')
    list_filter = ('role', 'is_active', 'is_staff')

    fieldsets = UserAdmin.fieldsets + (
        (None, {
            'fields': ('phone_number', 'national_code', 'address', 'role')
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {
            'fields': ('phone_number', 'national_code', 'address', 'role')
        }),
    )

    search_fields = ('username', 'first_name', 'last_name', 'phone_number', 'national_code')
    ordering = ('id',)

    def full_name(self, obj):
        return obj.full_name
    full_name.short_description = 'Full Name'
