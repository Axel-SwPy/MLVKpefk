from django.contrib import admin
from .models import *


class NewsAdmin(admin.ModelAdmin):
    list_display = ("id", "title","content", "photo")

admin.site.register(News, NewsAdmin)

