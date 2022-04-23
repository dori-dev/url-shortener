from django.contrib import admin
from .models import Url


class UrlAdmin(admin.ModelAdmin):
    search_fields = ["uuid", "link"]
    list_display = ["link", "uuid"]


admin.site.register(Url, UrlAdmin)
