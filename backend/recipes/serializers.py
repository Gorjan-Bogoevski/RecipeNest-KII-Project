from rest_framework import serializers
from .models import Recipe

class RecipeSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    title = serializers.CharField()
    ingredients = serializers.ListField(child=serializers.CharField())
    steps = serializers.ListField(child=serializers.CharField())
    cook_time = serializers.IntegerField()
    tags = serializers.ListField(child=serializers.CharField())
    image_url = serializers.URLField()

    def create(self, validated_data):
        return Recipe(**validated_data).save()

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance

