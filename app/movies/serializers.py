from rest_framework import serializers
from .models import Movies


class MoviesSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True)
    genre = serializers.CharField(required=True)
    director = serializers.CharField(required=True)
    cast = serializers.CharField(required=True)

    class Meta:
        model = Movies
        fields = ("id", "title", "genre", "cast", "director")

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.genre = validated_data.get("genre", instance.genre)
        instance.cast = validated_data.get("cast", instance.cast)
        instance.director = validated_data.get("director", instance.director)
        instance.save()
        return instance
