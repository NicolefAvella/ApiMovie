from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from movies.models import Movies
from movies.serializers import MoviesSerializer
from django.contrib.auth.models import User


class BaseViewTest(APITestCase):
    client = APIClient()

    def create_movie(title="", genre="", cast="", director=""):
        if title != "" and genre != "" and cast!= "" and director != "":
            Movies.objects.create(title=title, genre=genre, cast=cast, director=director)

    def setUp(self):
        """Add test data"""
        self.create_movie("Fast_and_Furious", "Action", "Dwayne_Johnson")
        self.create_movie("The_lion_king", "Drama", "Donal_Glover")
        self.create_movie("The_mummy", "Horror", "Brendan_Fraser")



class GetAllMoviesTest(BaseViewTest):

    def test_get_all_movies(self):
        """
        This test ensures that all movies added in the setUp method
        exist when we make a GET request to the movies/ endpoint
        """

        response = self.client.get(
            reverse("movies-all")
        )

        expected = Movies.objects.all()
        serialized = MoviesSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
