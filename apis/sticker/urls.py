"""Rides URLs."""

# Django
from django.urls import include, path


# Third party integration
from rest_framework import routers

from apis.sticker.views import StickerViewSet

router = routers.SimpleRouter()
router.register(r"sticker", StickerViewSet, basename="sticker")
urlpatterns = [
    path("", include(router.urls)),
]
