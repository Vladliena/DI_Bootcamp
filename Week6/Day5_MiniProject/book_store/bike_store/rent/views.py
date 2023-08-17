from django.shortcuts import render
from django.shortcuts import render
from rest_framework import status
from .models import Customer,Vehicle,VehicleType,VehicleSize,Rental,RentalRate,RentalStation,Address,VehicleAtRentalStation
from .serializers import (
    CustomerSerializer,
    VehicleSerializer,
    VehicleTypeSerializer,
    VehicleSizeSerializer,
    RentalSerializer,
    RentalRateSerializer,
    RentalStationSerializer,
    AddressSerializer,
    VehicleAtRentalStationSerializer
)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
# Create your views here.

class RentalView(APIView):
    
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        rentals = Rental.objects.all()
        serializer = RentalSerializer(rentals, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RentalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CustomerView(APIView):
    
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        rentals = Customer.objects.all()
        serializer = CustomerSerializer(rentals, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class VehicleView(APIView):
    
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        rentals = Vehicle.objects.all()
        serializer = VehicleSerializer(rentals, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = VehicleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class VehicleTypeView(APIView):
    
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        rentals = VehicleType.objects.all()
        serializer = VehicleTypeSerializer(rentals, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = VehicleTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class VehicleSizeView(APIView):
    
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        rentals = VehicleSize.objects.all()
        serializer = VehicleSizeSerializer(rentals, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = VehicleSizeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class RentalRateView(APIView):
    
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        rentals = RentalRate.objects.all()
        serializer = RentalRateSerializer(rentals, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RentalRateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class RentalStationView(APIView):
    
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        rentals = RentalStation.objects.all()
        serializer = RentalStationSerializer(rentals, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RentalStationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class AddressView(APIView):
    
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        rentals = Address.objects.all()
        serializer = AddressSerializer(rentals, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class VehicleAtRentalStationView(APIView):
    
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        rentals = VehicleAtRentalStation.objects.all()
        serializer = VehicleAtRentalStationSerializer(rentals, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = VehicleAtRentalStationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
