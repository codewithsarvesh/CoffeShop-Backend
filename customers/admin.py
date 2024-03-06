from django.contrib import admin
from customers.models import User
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone')

admin.site.register(User,UserAdmin)
