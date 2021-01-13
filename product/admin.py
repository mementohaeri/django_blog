from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'stock_quan', 'price']
    list_display_links = ['name']

    def count_text(self, obj):
        return '{}글자'.format(len(obj.text))
    count_text.short_description = 'Post 글자수'
    
admin.site.register(Post, PostAdmin)
