from rest_framework import serializers
from app.models import Movie, Rater, Rating

class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ("movie_title", "release_date", "video_release_date", "IMDb_URL", "unknown",
"action", "adventure", "animation", "childrens", "comedy", "crime", "documentary",
"drama", "fantasy", "film_noir", "horror", "musical", "mystery", "romance", "sci_fi",
"thriller", "war", "western")


class RaterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rater
        fields = ("age", "gender", "occupation", "zip_code")



class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = ("user", "item", "rating", "timestamp")
        depth = 1
