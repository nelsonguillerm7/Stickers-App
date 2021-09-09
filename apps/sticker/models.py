from django.db import models


# Create your models here.
class StickerCategory(models.Model):
    """Model create sticker category"""

    class TypeAnimated(models.TextChoices):
        ANIMATED = "Animated", "Animated"
        NOT_ANIMATED = "Not Animated", "Not Animated"

    name = models.CharField(max_length=128)
    type_animated = models.CharField(
        max_length=64,
        choices=TypeAnimated.choices,
        default=TypeAnimated.ANIMATED,
    )

    class Meta:
        """Class information"""

        verbose_name = "Stickers Category"
        verbose_name_plural = "Sticker Categories"

    def __str__(self):
        return f"{self.name}"


class StickerImage(models.Model):
    """Model create sticker image"""

    category = models.ForeignKey(
        "sticker.StickerCategory", on_delete=models.PROTECT, related_name="stickers"
    )
    img = models.FileField(upload_to="sticker")

    class Meta:
        """Class information"""

        verbose_name = "Stickers Image"
        verbose_name_plural = "Stickers Images"

    def __str__(self):
        return f"Sticker {self.id}"
