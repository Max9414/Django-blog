from django.contrib import admin
from .models import About
from django_summernote.admin import SummernoteModelAdmin

@admin.register(About)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'created_on')
    summernote_fields = ('body')

# Register your models here.