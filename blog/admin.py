from django.contrib import admin
from .models import Post, Category,AboutUs

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content','created_at')  # Ensure all necessary fields are displayed
    search_fields=('title','created_at')
    
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(AboutUs)
