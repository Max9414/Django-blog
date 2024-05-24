from django.contrib import admin
from .models import About, CollaborateRequest
from django_summernote.admin import SummernoteModelAdmin

@admin.register(About)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'created_on')
    summernote_fields = ('body')

@admin.register(CollaborateRequest)
class CollaborateRequestAdmin(admin.ModelAdmin):

    list_display = ('message', 'read',)

# Register your models here.