from django.contrib import admin
from .models import Blog, Service

@admin.register(Blog)
class BlogModelAdmin(admin.ModelAdmin):
    list_display = ("titre","description","image","date")


@admin.register(Service)
class ServiceModelAdmin(admin.ModelAdmin):
    list_display = ("titre","description","image",)