from rest_framework.test import APITestCase
from movies.models import Movies


class MoviesModelTest(APITestCase):
    def setUp(self):
        self.a_movie = Movies.objects.create(
            title = "Fast_and_Furious",
            genre = "Action",
            cast = "Dwayne_Johnson",
            director = "st",
        )

    def test_movies(self):
        """Test movie in setup exist"""

        self.assertEqual(self.a_movie.title, "Fast_and_Furious")
        self.assertEqual(self.a_movie.genre, "Action")
        self.assertEqual(self.a_movie.cast, "Dwayne_Johnson")
        self.assertEqual(self.a_movie.director, "st")
