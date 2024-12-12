from django.contrib import admin, messages
from django.core.exceptions import ValidationError
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
        try:
            # Check if file was uploaded
            if not obj.file:
                raise ValidationError('A PDF file is required')

            # Check if it's a PDF file
            file_name = str(obj.file)
            if not file_name.lower().endswith('.pdf'):
                raise ValidationError('Only PDF files are allowed')

            super().save_model(request, obj, form, change)
            messages.success(request, 'Tab successfully saved.')
            
        except ValidationError as e:
            messages.error(request, str(e))
            return False

    def response_add(self, request, obj, post_url_continue=None):
        """
        Determines the response after adding an object.
        """
        if '_addanother' not in request.POST and '_continue' not in request.POST:
            messages.success(request, 'Tab successfully added.')
        return super().response_add(request, obj, post_url_continue)


admin.site.register(Review)
