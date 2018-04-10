from django.contrib import admin
from models import Category, Page
# Register your models here.

# Add in this class to customise the Admin Interface
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

class PageAdmin(admin.ModelAdmin):
    """docstring for PageAdmin"""
    list_display = ('title','category', 'url')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)