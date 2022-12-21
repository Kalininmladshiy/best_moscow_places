from django.contrib import admin

from .models import Place, Image
from django.utils.html import format_html
from adminsortable2.admin import SortableAdminBase, SortableTabularInline
from adminsortable2.admin import SortableAdminMixin


class PlaceImageInline(SortableTabularInline):
    model = Image
    readonly_fields = ('get_preview',)
    fields = ['position', 'picture', 'get_preview']
    extra = 1

    def get_preview(self, place):
        return format_html('<img src="{url}" width="{width}" height={height} />',
            url=place.picture.url,
            width=(place.picture.width / 3),
            height=(place.picture.height / 3),
         )


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ('title', 'description_short')
    inlines = [PlaceImageInline]


@admin.register(Image)
class ImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass
