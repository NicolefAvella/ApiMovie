from rest_framework import generics
from .models import Movies
from .serializers import MoviesSerializer


class ListMoviesView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer
