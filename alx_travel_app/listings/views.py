from django.shortcuts import render
from rest_framework import viewsets
from .models import User, Listing, Booking, Review
from .serializers import ListingSerializer, BookingSerializer
from django.http import JsonResponse


# Create your views here.
class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    
    
    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.query_params('name')
        description = self.request.query_params('description')
        location = self.request.query_params('location')
        
        if name:
            queryset = queryset.filter(genre__iexact=name)
        if description:
            queryset = queryset.filter(genre__iexact=description)
        return queryset
            
        
