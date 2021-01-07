from rest_framework import serializers
from webapp.models import Theatre, Movie, Show, Booking, Seat, BookedSeat


class WebSerializer(serializers.ModelSerializer):

    movie_name = serializers.CharField(read_only=True, source='movie.name')
    movie_director = serializers.CharField(read_only=True, source='movie.director')
    movie_trailer = serializers.CharField(read_only=True, source='movie.trailer')
    movie_language = serializers.CharField(read_only=True, source='movie.language')
    theatre_name = serializers.CharField(read_only=True, source='theatre.name')
    theatre_city = serializers.CharField(read_only=True, source='theatre.city')
    theatre_address = serializers.CharField(read_only=True, source='theatre.address')
    theatre_no_of_screen = serializers.CharField(read_only=True, source='theatre.no_of_screen')

    class Meta:
        model = Show
        fields = ['movie_name', 'movie_trailer', 'movie_language', 'movie_director', 'theatre_name', 'theatre_city', 'theatre_address', 'theatre_no_of_screen', 'date', 'time']