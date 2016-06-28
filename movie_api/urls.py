"""movie_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app.views import MovieListAPIView, MovieDetailAPIView, RaterListAPIView
from app.views import RaterDetailAPIView, RatingListAPIView, RatingDetailAPIView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/movies/$', MovieListAPIView.as_view(), name="movie_list_api_view"),
    url(r'^api/movies/(?P<pk>\d+)/$', MovieDetailAPIView.as_view(), name="movie_detail_api_view"),
    url(r'^api/rater/$', RaterListAPIView.as_view(), name="rater_list_api_view"),
    url(r'^api/rater/(?P<pk>\d+)/$', RaterDetailAPIView.as_view(), name="rater_detail_api_view"),
    url(r'^api/rating/$', RatingListAPIView.as_view(), name="rating_list_api_view"),
    url(r'^api/rating/(?P<pk>\d+)/$', RatingDetailAPIView.as_view(), name="rating_detail_api_view")
]
