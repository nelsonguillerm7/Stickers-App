from rest_framework import serializers

from apps.sticker.models import StickerCategory, StickerImage


class ImagesSerializers(serializers.ModelSerializer):
    class Meta:
        model = StickerImage
        fields = ("id", "img")


class StickerSerializers(serializers.ModelSerializer):
    stickers = ImagesSerializers(many=True)

    class Meta:
        model = StickerCategory
        fields = (
            "id",
            "name",
            "type_animated",
            "stickers",
        )
