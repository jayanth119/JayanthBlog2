from django.contrib import admin
from .models import Category, Post


# Register your models here.

# for configuration of Category admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('image_tag', 'title', 'description', 'url', 'add_date')
    search_fields = ('title',)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    list_filter = ('cat',)
    list_per_page = 50

    class Media:
        js = ('https://cdn.tiny.cloud/1/5saa333fagujw6f8q79tmbxohvt9ejijwda5zq9o96pm8497/tinymce/6/tinymce.min.js', 'js/ss.js',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
