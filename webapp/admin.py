from django.contrib import admin

from .models import Tool

@admin.register(Tool)
class ToolAdmin(admin.ModelAdmin):

    list_display = (
        'slug',
        'tool_title',
        'tool_iframe_url',
        'tool_supporting_script_source'
    )
