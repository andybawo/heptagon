from django.contrib import admin
from .models import *
# Register your models here.

class showlogin(admin.ModelAdmin):
    list_display=('createname','createemail','createusername','createpassword')
admin.site.register(login,showlogin)