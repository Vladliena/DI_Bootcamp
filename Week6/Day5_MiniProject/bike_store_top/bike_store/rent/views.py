from django.shortcuts import render
from django.shortcuts import render
from django.db.models import Count
from django.db.models.functions import TruncMonth
from rest_framework import status
from .models import (
    Customer,
    Vehicle,
    VehicleType,
    VehicleSize,
    Rental,
    RentalRate,
    RentalStation,
    Address,
    VehicleAtRentalStation,
)
from .serializers import (
    CustomerSerializer,
    VehicleSerializer,
    VehicleTypeSerializer,
    VehicleSizeSerializer,
    RentalSerializer,
    RentalRateSerializer,
    RentalStationSerializer,
    AddressSerializer,
    VehicleAtRentalStationSerializer,
)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

# Create your views here.


class RentalView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk=None, format=None):
        if pk is None:
            rentals = Rental.objects.order_by("return_date", "rental_date")
            serializer = RentalSerializer(rentals, many=True)
            return Response(serializer.data)
        else:
            rental = Rental.objects.get(id=pk)
            serializer = RentalSerializer(rental)
            return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RentalSerializer(data=request.data)

        if serializer.is_valid():
            customer_id = serializer.validated_data["customer"].id
            vehicle_id = serializer.validated_data["vehicle"].id
            if not Customer.objects.filter(id=customer_id).exists():
                return Response(
                    {"error": "Customer does not exist."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            if not Vehicle.objects.filter(id=vehicle_id).exists():
                return Response(
                    {"error": "Vehicle does not exist."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            if Rental.objects.filter(
                vehicle_id=vehicle_id, return_date__isnull=True
            ).exists():
                return Response(
                    {"error": "Vehicle is currently rented."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, *args, **kwargs):
        rental = Rental.objects.get(id=pk)
        serializer = RentalSerializer(instance=rental, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, pk, *args, **kwargs):
        rental = Rental.objects.get(id=pk)
        rental.delete()
        return Response({"Message": f"deleted {rental.vehicle} of {rental.customer}"})


class CustomerView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, action=None, *args, **kwargs):
        if action == "add":
            return self.post(request)

        customers = Customer.objects.all().order_by("first_name")
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VehicleView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk=None, action=None, *args, **kwargs):
        if action == "add":
            return self.post(request)
        elif pk is None:
            vehicles = Vehicle.objects.all().order_by("vehicle_type")
            serializer = VehicleSerializer(vehicles, many=True)
            return Response(serializer.data)
        else:
            vehicle = Vehicle.objects.get(id=pk)
            serializer = VehicleSerializer(vehicle)
            return Response(serializer.data)

    def post(self, request, format=None):
        serializer = VehicleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, *args, **kwargs):
        vehicle = Vehicle.objects.get(id=pk)
        serializer = VehicleSerializer(instance=vehicle, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, pk, *args, **kwargs):
        vehicle = Vehicle.objects.get(id=pk)
        vehicle.delete()
        return Response({"Message": f"deleted {vehicle.vehicle_type}"})


class RentalStationView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk=None, action=None, *args, **kwargs):
        if action == "add":
            return self.post(request)

        if pk is None:
            rentals = RentalStation.objects.all()
            serializer = RentalStationSerializer(rentals, many=True)
            return Response(serializer.data)
        else:
            rental = RentalStation.objects.get(id=pk)
            serializer = RentalStationSerializer(rental)
            return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RentalStationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        station = RentalStation.objects.get(id=pk)
        station.delete()
        return Response({"Message": f"deleted {station.name}"})


class MonthlyStatsView(APIView):
    def get(self, request, format=None):
        monthly_stats = (
            Rental.objects.annotate(month=TruncMonth("rental_date"))
            .values("month")
            .annotate(rental_count=Count("id"))
            .order_by("month")
        )

        stats_data = {
            item["month"].strftime("%Y-%m"): item["rental_count"]
            for item in monthly_stats
        }

        return Response(stats_data)


class PopularStationView(APIView):
    def get(self, request, format=None):
        popular_stations = RentalStation.objects.annotate(
            rental_count=Count("address")
        ).order_by('-rental_count')

        station_stats = {
            station.name: station.rental_count for station in popular_stations
        }

        return Response(station_stats)
    
class PopularVehicleTypeView(APIView):
    def get(self, request, format=None):
        vehicle_type_stats = VehicleType.objects.annotate(
            rental_count=Count('vehicle')
        ).order_by('-rental_count')

        type_stats = {vehicle_type.name: vehicle_type.rental_count for vehicle_type in vehicle_type_stats}

        return Response(type_stats)
