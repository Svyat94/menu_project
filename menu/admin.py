from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from mptt.admin import DraggableMPTTAdmin
from .models import Category, Article


class CustomCategoryAdmin(DraggableMPTTAdmin, MPTTModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = (
        'tree_actions',
        'indented_title',
    )
    list_display_links = (
        'indented_title',
    )


admin.site.register(Category, CustomCategoryAdmin)
admin.site.register(Article)
