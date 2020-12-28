from django.shortcuts import render
from rest_framework import generics

from locale_backend.core.models import *
from locale_backend.core.serializers import * 

# Create your views here.
class BookingListCreateView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
