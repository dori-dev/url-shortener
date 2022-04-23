from django.contrib import admin
from .models import Url


class UrlAdmin(admin.ModelAdmin):
    search_fields = ["uuid", "link"]
    list_display = ["short_link", "uuid"]

    def short_link(self, model: Url):
        short = model.link[:64]
        if short != model.link:
            return f"{short}..."
        return short


admin.site.register(Url, UrlAdmin)
