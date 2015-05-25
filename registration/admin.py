from django.contrib import admin
from .models import Registration, Contact


class UserInfo(admin.StackedInline):
    model = Contact
    extra = 1


class UserInfoPosition(admin.ModelAdmin):
    search_fields = ['email']
    list_display = ['id','login', 'email']

    fieldsets = [
        ('New User Registration', {'fields': ['login', 'email', 'password', 'repeat_password']})
    ]

    inlines = [UserInfo]

admin.site.register(Registration, UserInfoPosition)