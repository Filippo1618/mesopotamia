from django.contrib import admin
from django.db import models
from .models import BlogPost

# Register your models here.

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title","value","desc", "new", "active")

admin.site.register(BlogPost, BlogPostAdmin)