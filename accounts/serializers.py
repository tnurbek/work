from rest_framework import serializers
from .models import Image, Log


class ImageSerializer(serializers.ModelSerializer):
    # user = serializers.StringRelatedField()
    class Meta:
        model = Image
        fields = '__all__'


class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = '__all__'