from rest_framework import serializers
from .models import Tutorial


class TutorialSerializers(serializers.ModelsSerializers):
    class Meta:
        model = Tutorial
        fields = ["id", "title", "content", "published_date"]