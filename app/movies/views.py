from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import status

from django.core.exceptions import ObjectDoesNotExist

from .models import Movies, Recomment
from .data import ACTION
from .serializers import MoviesSerializer


class ListMoviesView(generics.ListCreateAPIView):
    """
    Provides a get method handler.
    """
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer

    def post(self, request, *args, **kwargs):
        """Create a movie http post"""
        a_movie = Movies.objects.create(
            title=request.data["title"],
            genre=request.data["genre"],
            cast=request.data["cast"],
            director=request.data["director"],
            user=request.user
        )
        return Response(
            data=MoviesSerializer(a_movie).data,
            status=status.HTTP_201_CREATED
        )


class MoviesDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Get detail, put and delete movie """

    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer

    # detail
    def get(self, request, *args, **kwargs):
        try:
            a_movie = self.queryset.get(pk=kwargs["pk"])
            return Response(MoviesSerializer(a_movie).data)
        except Movies.DoesNotExist:
            return Response(
                data={
                    "message": "Movie with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    # edit
    def put(self, request, *args, **kwargs):
        """Edit a movie"""
        try:
            instance = self.get_object()

            if instance.user != request.user:
                return Response(
                    data={
                        "message": "No unauthorized"
                    },
                    status=status.HTTP_401_UNAUTHORIZED
                )
            serializer = MoviesSerializer()
            updated_movie = serializer.update(instance, request.data)
            return Response(MoviesSerializer(updated_movie).data)

        except Movies.DoesNotExist:
            return Response(
                data={
                    "message": "Movie with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )


    def delete(self, request, *args, **kwargs):
        """Delete a movie"""
        try:
            instance = self.get_object()

            if instance.user != request.user:
                return Response(
                    data={
                        "message": "No unauthorized"
                    },
                    status=status.HTTP_401_UNAUTHORIZED
                )
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        except Movies.DoesNotExist:
            return Response(
                data={
                    "message": "Movie with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

class RecommentView(generics.ListAPIView):
    """Recomment movie, filter genre"""
    serializer_class = MoviesSerializer

    def get_queryset(self):
        filter = self.request.query_params.get('genre', ACTION)

        return Movies.objects.filter(genre__iexact=filter)
