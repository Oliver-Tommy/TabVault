from django.contrib import admin
from .models import Tab, Review
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Tab)
class TabAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'created_at')
    search_fields = ['title']
    list_filter = ('difficulty', 'genre',)
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('views',)


# Register your models here.

admin.site.register(Review)