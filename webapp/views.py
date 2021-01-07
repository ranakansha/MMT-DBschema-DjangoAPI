from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from webapp.serializers import WebSerializer
from webapp.models import Theatre, Movie, Show, Booking, Seat, BookedSeat
from rest_framework import status

# Create your views here.
@api_view(['GET'])
def city_list(request):
    if request.method =="GET":
        city = request.GET.get('city')
        obj = Show.objects.filter(theatre__city=city).order_by('movie')
        serializer = WebSerializer(obj,many=True)
        return Response(serializer.data)
