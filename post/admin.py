# Basic Django Modules
from django.contrib import admin

# Custom Models
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "content", "created_at", "hits")


admin.site.register(Comment)
