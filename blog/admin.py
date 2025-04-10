from django.contrib import admin
from .models import Category, Post




class PostAdmin(admin.ModelAdmin):
    list_display = ("title","content","date","category")
    list_display_links = ("title",)
    search_fields = ("title",)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_display_links = ("name",)
    search_fields = ("name",)

admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)

