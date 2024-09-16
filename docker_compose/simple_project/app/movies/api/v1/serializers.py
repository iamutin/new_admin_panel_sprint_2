from rest_framework import serializers

from ...models import FilmWork


class FilmWorkSerializer(serializers.ModelSerializer):
    genres = serializers.StringRelatedField(many=True, read_only=True)
    actors = serializers.ListField()
    directors = serializers.ListField()
    writers = serializers.ListField()

    class Meta:
        model = FilmWork
        fields = (
            'id',
            'title',
            'description',
            'creation_date',
            'rating',
            'type',
            'genres',
            'actors',
            'directors',
            'writers',
        )

    def to_representation(self, instance):
        data = super().to_representation(instance)
        for key in data:
            if key in ('actors', 'directors', 'writers'):
                data[key] = data[key] or []
        return data
