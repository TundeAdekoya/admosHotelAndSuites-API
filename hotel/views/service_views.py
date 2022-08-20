from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response 
from django.contrib.auth.models import User 

from hotel.models import *
from hotel.serializers import *

from rest_framework import status
# Create your views here.

@api_view(['GET'])
def bookRooms(request):
    rooms = Room_service.objects.all()
    serializer = Room_serviceSerializer(rooms, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def bookRoom(request, pk):
    room = Room_service.objects.get(_id=pk)
    serializer = Room_serviceSerializer(room, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def bookEvents(request):
    events = Event_service.objects.all()
    serializer = Event_serviceSerializer(events, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def bookEvent(request, pk):
    event = Event_service.objects.get(_id=pk)
    serializer = Event_serviceSerializer(event, many=False)
    return Response(serializer.data)