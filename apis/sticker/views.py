from rest_framework import viewsets

from apis.sticker.serializers import StickerSerializers
from apps.sticker.models import StickerCategory


class StickerViewSet(viewsets.ModelViewSet):
    queryset = StickerCategory.objects.all()
    serializer_class = StickerSerializers
