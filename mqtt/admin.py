from django.contrib import admin

from mqtt.models import CollarData


@admin.register(CollarData)
class CollarDataAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CollarData._meta.fields]
    ordering = ['id']
    list_display_links = ['id']
    search_fields = ('topic',)