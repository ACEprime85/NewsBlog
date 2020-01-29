from django.contrib import admin
from django.db import models
from . models import Blogpost, Comment, Video


#models.

class BlogpostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'published_date',
                    'status')

    
    list_filter = ('status', 'published_date', 'publish', 'author')    
    search_fields = ('title', 'body')    
    prepopulated_fields = {'slug': ('title',)}    
    raw_id_fields = ('author',)    
    date_hierarchy = 'publish'    
    ordering = ['status', 'publish']


class CommentAdmin(admin.ModelAdmin):    
    list_display = ('name', 'email', 'post', 'created', 'active')    
    list_filter = ('active', 'created', 'updated')    
    search_fields = ('name', 'email', 'body') 






admin.site.register(Video)
admin.site.register(Blogpost, BlogpostAdmin)
admin.site.register(Comment, CommentAdmin)