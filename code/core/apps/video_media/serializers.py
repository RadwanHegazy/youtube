from rest_framework import serializers
from .models import VideoMedia


class VideoMediaSerializer(serializers.ModelSerializer) : 

    class Meta:
        model = VideoMedia
        fields = [
            'quality',
            'path'
        ]