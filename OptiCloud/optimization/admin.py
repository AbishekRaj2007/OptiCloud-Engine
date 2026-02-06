from django.contrib import admin

# Register your models here.

from .models import ResourceUsage

admin.site.register(ResourceUsage)
