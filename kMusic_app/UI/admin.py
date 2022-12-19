from django.contrib import admin

from .models import User, Catalog
# Register your models here.

admin.site.register(User)
admin.site.register(Catalog)
