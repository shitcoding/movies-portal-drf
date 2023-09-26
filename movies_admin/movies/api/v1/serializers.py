from rest_framework import serializers

from movies.models import Filmwork, PersonFilmwork


class FilmworkSerializer(serializers.ModelSerializer):
    genres = serializers.SerializerMethodField()
    actors = serializers.SerializerMethodField()
    directors = serializers.SerializerMethodField()
    writers = serializers.SerializerMethodField()

    class Meta:
        model = Filmwork
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

    def get_genres(self, obj):
        return [genre.name for genre in obj.genres.all()]

    def get_actors(self, obj):
        return [
            pfw.person.full_name
            for pfw in PersonFilmwork.objects.filter(
                film_work=obj, role='actor'
            )
        ]

    def get_directors(self, obj):
        return [
            pfw.person.full_name
            for pfw in PersonFilmwork.objects.filter(
                film_work=obj, role='director'
            )
        ]

    def get_writers(self, obj):
        return [
            pfw.person.full_name
            for pfw in PersonFilmwork.objects.filter(
                film_work=obj, role='writer'
            )
        ]
