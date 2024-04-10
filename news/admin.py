from django.contrib import admin
from django.contrib.admin.sites import site
from news.models import news


class newsAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'date')
     
admin.site.register(news, newsAdmin)

