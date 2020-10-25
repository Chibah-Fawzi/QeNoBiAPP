from django.contrib import admin

# Register your models here.

from .models import Group, Link

admin.site.register(Group)

admin.site.register(Link)
