from .models import Advertisment, Responses
from rest_framework import serializers


class AdsSerializer(serializers.Serializer):
    head = serializers.CharField(max_length=255)
    content_upload = serializers.CharField()
    category = serializers.CharField()
    user_id = serializers.IntegerField()
