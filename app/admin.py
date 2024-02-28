from django.contrib import admin
from .models import *

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'photo', 'author', 'founder_contact', 'data')
    search_fields = ('id', 'name', 'founder_contact', 'author', 'data')
    list_editable = ('photo', 'founder_contact')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'text', 'author', 'data')
    search_fields = ('id', 'post', 'text', 'author', 'data')

class FeedbackMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'text', 'data')
    search_fields = ('id', 'email', 'text', 'data')

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(FeedbackMessage, FeedbackMessageAdmin)

# Register your models here.
