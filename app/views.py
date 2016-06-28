from django.shortcuts import render
from app.models import Movie, Rater, Rating
from django.views.generic import View
from rest_framework import generics
from app.serializers import MovieSerializer, RaterSerializer, RatingSerializer


class MovieListAPIView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class RaterListAPIView(generics.ListCreateAPIView):
    queryset = Rater.objects.all()
    serializer_class = RaterSerializer


class RaterDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rater.objects.all()
    serializer_class = RaterSerializer


class RatingListAPIView(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


class RatingDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
