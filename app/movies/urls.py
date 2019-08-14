from django.urls import path
from .views import ListMoviesView, MoviesDetailView


urlpatterns = [
    path('movies/', ListMoviesView.as_view(), name="movies-all"),
    path('movies/<int:pk>/', MoviesDetailView.as_view(), name="movies-detail"),
]
