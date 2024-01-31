from django.contrib import admin
from news.models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['image', 'title', 'date', 'content']
    search_fields = ['title', 'content']

