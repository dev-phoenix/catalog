from django.contrib import admin
from django.contrib.auth.models import Group
from django.utils.safestring import mark_safe
from django.utils.html import format_html
from .models import *
import json

admin.site.unregister(Group)
admin.site.site_header = "Админ панель"
admin.site.site_title = "Админ панель"
admin.site.index_title = "Добро пожаловать"



### КОНСТРУКТОР АНКЕТЫ ###
class CategoryAdmin(admin.ModelAdmin):
    """Модель категории"""

    list_display = ['parent','weight','name','key']
    search_fields = ['parent','weight','name','key']
    list_filter = ['parent','weight','name','key']

    class Meta:
        model = Category

admin.site.register(Category, CategoryAdmin)
### КОНСТРУКТОР АНКЕТЫ ###