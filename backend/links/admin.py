from django.contrib import admin
from links.models import Link

from django.utils.safestring import mark_safe
from django.template.loader import render_to_string


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'link',
        'show_on_home',
        'visitar'
    )

    def visitar(self, obj: Link) -> str:
        return mark_safe(
            render_to_string('redirect-button.html', {
                'link': obj.link
            })
        )
