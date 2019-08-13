from rest_framework import serializers
from .models import Movies


class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = ("title", "genre", "cast", "director")

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.genre = validated_data.get("title", instance.genre)
        instance.cast = validated_data.get("title", instance.cast)
        instance.director = validated_data.get("title", instance.director)
        instance.save()
        return instance
