from django.contrib import admin
from django.db.models import fields
from .models import Todo

# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    list_display = ('name','priority','completed')

admin.site.register(Todo,TodoAdmin)