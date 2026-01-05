from django.contrib import admin
from .models import Category,Blog
"""this code is used to automatically add the sulg value when we add the tilte which help in the url(searching)"""
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    list_display = ('title','category','author','is_featured','status') # to show extra columns in the admin panel
    search_fields = ('id','title','category__category_name','status')
    list_editable = ('is_featured',)

# Register your models here.
admin.site.register(Category)
admin.site.register(Blog,BlogAdmin)