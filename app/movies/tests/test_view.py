from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from movies.models import Movies
from movies.serializers import MoviesSerializer
from  user.models import User
import json


class BaseViewTest(APITestCase):
    client = APIClient()

    def create_movie(self, title="", genre="", cast="", director=""):
        """create a movie"""
        if title != "" and genre != "" and cast!= "" and director != "":
            return Movies.objects.create(title=title, genre=genre, cast=cast, director=director)
        else:
            print("faltan datos")

    def movie_request(self, kind="post", **kwargs):
        """Post create movie and put"""
        if kind == "post":
            return self.client.post(reverse("movies-all"),
            data=json.dumps(kwargs["data"]),
            content_type='application/json'
            )

        elif kind == "put":
            return self.client.put(
                reverse(
                    "movies-detail",
                    kwargs={"pk" : kwargs["id"]}
                ),
            data=json.dumps(kwargs["data"]),
            content_type='application/json'
            )
        else:
            return None

    def retrieve_movie(self, pk=0):
        return self.client.get(
            reverse(
                "movies-detail",
                kwargs={"pk" : pk}
                )
        )

    def delete_movie(self, pk=0):
        return self.client.delete(
            reverse(
                "movies-detail",
                kwargs={"pk" : pk}
                )
        )


    def setUp(self):
        """Add test data"""
        self.movie_1 = self.create_movie(title="Fast_and_Furious", genre="Action", cast="Dwayne_Johnson", director="flata")
        self.create_movie(title="The_lion_king", genre="Drama", cast="Donal_Glover", director='st')
        self.create_movie(title="The_mummy", genre="Horror", cast="Brendan_Fraser", director='md')

        self.valid_movie_id = self.movie_1.id
        self.invalid_movie_id = 50

        """create a user"""
        self.user = User.objects.create_superuser(
            username="test",
            email="test@gmail.com",
            password="test123",
            first_name="first name",
            last_name="last name",
            is_active=True,
        )

        url = reverse('user:login')
        data = {
            "email": "test@gmail.com",
            "password": "test123",
        }
        res = self.client.post(url, data=data, format='json')
        self.assertEqual(res.status_code, status.HTTP_200_OK, res.content)
        token=res.json().get('token')

        self.client.credentials(HTTP_AUTHORIZATION='Bearer {0}'.format(token))


class GetAllMoviesTest(BaseViewTest):

    def test_get_all_movies(self):
        """
        This test ensures that all movies added in the setUp method
        exist when we make a GET request to the movies/ endpoint
        """
        #self.login_client("test@gmail.com", "test123")
        response = self.client.get(
            reverse("movies-all")
        )

        expected = Movies.objects.all()
        serialized = MoviesSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetASingleMovieTest(BaseViewTest):

    def test_get_a_movie(self):
        """Test movie with id exist"""
        #self.login_client("test@gmail.com", "test123")
        response = self.retrieve_movie(self.valid_movie_id)
        expected = Movies.objects.get(pk=self.valid_movie_id)
        serialized = MoviesSerializer(expected)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.retrieve_movie(self.invalid_movie_id)# ??
        self.assertEqual(
            response.data["message"],
            "Movie with id: 50 does not exist"
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
