from .models import *
from django.contrib import admin


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('image_tag','title', 'description', 'url',)
    search_fields = ("title",)
    list_filter = ('title',)
admin.site.register(Category, CategoryAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ("title",)
    list_filter = ('title',)
    class Media:
        js = ("js/script.js",)



admin.site.register(Post, PostAdmin)
