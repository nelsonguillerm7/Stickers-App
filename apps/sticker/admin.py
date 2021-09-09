from django.contrib import admin

# Register your models here.
from apps.sticker.models import StickerCategory, StickerImage


class PresentationInline(admin.TabularInline):
    """Inline form for User Profile"""

    model = StickerImage
    extra = 1


@admin.register(StickerCategory)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [PresentationInline]
