from django.contrib import admin
from .models import Post, Category
from django.contrib.auth. models import User
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'post_date', 'category')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)