from django.shortcuts import get_object_or_404
from .models import Movies
from .serializers import MovieSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def get_movie_list(request):
    movies = Movies.objects.order_by('release_date')
    data = MovieSerializer(movies, many=True).data

    return Response(data)
@api_view(['GET', 'POST'])
def get_movie_detail(request,pk):
    movie = get_object_or_404(Movies,pk)
    data = MovieSerializer(movie).data
    return Response(data)