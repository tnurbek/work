from django.contrib import admin
from .models import Image, Log


class ImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'id', 'created_at')


class LogAdmin(admin.ModelAdmin):
    list_display = ('file', 'updated_at')


admin.site.register(Image, ImageAdmin)
admin.site.register(Log, LogAdmin)