from django.contrib import admin
from .models import Tool


@admin.register(Tool)
class ToolAdmin(admin.ModelAdmin):

    list_display = ("name","category","slug")

    prepopulated_fields = {"slug":("name",)}