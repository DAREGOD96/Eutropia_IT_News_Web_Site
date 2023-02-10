from django.contrib import admin
from .models import News

# Register your models here.

@admin.register(News)
class AdminModeNews(admin.ModelAdmin):
    list_display = ['news_title', 'news_image', 'news_description']