from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import status

from django.core.exceptions import ObjectDoesNotExist

from .models import Movies
from .serializers import MoviesSerializer


class ListMoviesView(generics.ListCreateAPIView):
    """
    Provides a get method handler.
    """
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer

    def post(self, request, *args, **kwargs):
        """Create a movie http post"""
        a_movie =Movies.objects.create(
            title=request.data["title"],
            genre=request.data["genre"],
            cast=request.data["cast"],
            director=request.data["director"],
        )
        return Response(
            data=MoviesSerializer(a_movie).data,
            status=status.HTTP_201_CREATED
        )

class MoviesDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Get detail, put and delete movie """

    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer

    def get(self, request, *args, **kwargs):
        try:
            a_movie = self.queryset.get(pk=kwargs["pk"])
            return Response(MoviesSerializer(a_movie).data)
        except Movies.DoesNotExit:
            return Response(
                data={
                    "message": "Movie with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def put(self, request, *args, **kwargs):
        try:
            a_movie = self.queryset.get(pk=kwargs["pk"])
            serializer = MoviesSerializer()
            updated_movie = serializer.update(a_movie, request.data)
            return Response(MoviesSerializer(updated_movie).data)
        except Movies.DoesNotExit:
            return Response(
                data={
                    "message": "Movie with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, *args, **kwargs):
        try:
            a_movie = self.queryset.get(pk=kwargs["pk"])
            a_movie.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Movies.DoesNotExit:
            return Response(
                data={
                    "message": "Movie with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )
