from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name',


class ImageAdmin(admin.ModelAdmin):
    list_display = 'title', 'category', 'user', 'created_at'
    ordering = 'created_at',



admin.site.register(models.User, UserAdmin)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Image, ImageAdmin)





