from django.contrib import admin, messages
from django_summernote.admin import SummernoteModelAdmin
from .models import Tab, Review


@admin.register(Tab)
class TabAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'created_at')
    search_fields = ['title']
    list_filter = ('difficulty', 'genre',)
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('views',)

    def save_model(self, request, obj, form, change):
        if not obj.file:
            messages.error(request, "A PDF file is required")
            return
        super().save_model(request, obj, form, change)


admin.site.register(Review)
