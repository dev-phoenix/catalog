from django.contrib import admin
from django.contrib.auth.models import Group
from django.utils.safestring import mark_safe
from django.utils.html import format_html
from .models import *
import json

# admin.site.unregister(Group)
# admin.site.site_header = "Админ панель"
# admin.site.site_title = "Админ панель"
# admin.site.index_title = "Добро пожаловать"



### КОНСТРУКТОР АНКЕТЫ ###
class NodeAdmin(admin.ModelAdmin):
    """Модель категории"""

    # list_display = ['categories','title','path','rating','desc']
    # search_fields = ['categories','title','path','rating','desc']
    # list_filter = ['categories','title','path','rating','desc']

    list_display = ['title','path','rating','desc']
    search_fields = ['title','path','rating','desc']
    list_filter = ['title','path','rating','desc']

    class Meta:
        model = Node

admin.site.register(Node, NodeAdmin)
### КОНСТРУКТОР АНКЕТЫ ###