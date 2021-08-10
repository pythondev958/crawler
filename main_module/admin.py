from django.contrib import admin

# Register your models here.

from .models import registration,login


admin.site.register(registration)
admin.site.register(login)