from django.contrib import admin
from apps.account.models import CustomUser, CustomUserManager
admin.site.register(CustomUser)