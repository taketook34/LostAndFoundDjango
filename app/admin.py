from django.contrib import admin
from .models import *

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'photo', 'founder_contact', 'data')
    search_fields = ('id', 'name', 'founder_contact', 'data')
    list_editable = ('photo', 'founder_contact')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'text', 'data')
    search_fields = ('id', 'post', 'text', 'data')

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)

# Register your models here.
