from django.db import models
from django.contrib.auth.models import Permission, User
from django.utils import timezone
from .data import TYPE_OPTIONS
from .data import ACTION
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

class Movies(models.Model):
    """Model of a movie
    A user can have many movies
    """

    #user = models.ForeignKey(User, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200, null=False)
    genre = models.CharField(max_length=50, choices=TYPE_OPTIONS, default=ACTION)
    year = models.CharField(max_length=4, null=True)
    cast = models.CharField(max_length=256)
    director = models.CharField(max_length=256)
    runtime = models.CharField(max_length=20, null=True)
    language = models.CharField(max_length=50, null=True)
    file = models.FileField(default='')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class ListMovies(models.Model):
    """List of prefered movies for de user
       A list can have many movies and
       A movie can be on many lists
    """
    #user_list = models.ForeignKey(User, default=User, on_delete=models.CASCADE)
    list_title = models.CharField(max_length=256)
    movies = models.ManyToManyField(Movies,blank=True)

    def __str__(self):
        return self.list_title


class Recomment(models.Model):
    movies = models.ForeignKey(Movies, on_delete=models.CASCADE)
    comments = models.TextField(max_length=500, default='What do you think of this movie', null=True)
    #user_comment = models.ForeignKey(User, on_delete=models.PROTECT)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    date_comment = models.DateField(auto_now_add=True)

    def __str__(self):
        return '{}-{}'.format(self.movies.title, str(self.movies.user))
