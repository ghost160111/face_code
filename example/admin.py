from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import (
    Contact
)

@admin.register(Contact)
class ContactModelAdmin(ModelAdmin):
    list_display = ['id', 'fullname', 'phone', 'created_at']
    list_display_links = ['id', 'fullname', 'phone', 'created_at']
    search_fields = ['id', 'fullname', 'phone']
    list_filter = ['fullname', 'phone']  