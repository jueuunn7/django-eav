from rest_framework import serializers


class BoardSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False)
    content = serializers.CharField(required=False)
