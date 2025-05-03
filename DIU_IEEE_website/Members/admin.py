from django.contrib import admin
from .models import MemberProfile, Projects

# Register your models here.
admin.site.register([
    MemberProfile,
    Projects,
])