from rest_framework import generics

from movies.api.v1.serializers import FilmworkSerializer
from movies.models import Filmwork


class MoviesListApi(generics.ListAPIView):
    queryset = Filmwork.objects.all()
    serializer_class = FilmworkSerializer


class MoviesDetailApi(generics.RetrieveAPIView):
    queryset = Filmwork.objects.all()
    serializer_class = FilmworkSerializer
