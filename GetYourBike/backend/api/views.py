from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProductSerializer, CategorySerializer, BicycleSerializer, RentBicycleSerializer, SaleBicycleSerializer, EquipmentSerializer, RentEquipmentSerializer, SaleEquipmentSerializer, ReservationRentSerializer, ReservationSaleSerializer, ReservationSerializer
from .models import Product, Category, Bicycle, RentBicycle, SaleBicycle, Reservation, RentEquipment, Equipment, SaleEquipment, ReservationRent, ReservationSale

# Create your views here.

#ListAPIView

class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class BicycleView(viewsets.ModelViewSet):
    queryset = Bicycle.objects.all()
    serializer_class = BicycleSerializer

class RentBicycleView(viewsets.ModelViewSet):
    queryset = RentBicycle.objects.all()
    serializer_class = RentBicycleSerializer

class SaleBicycleView(viewsets.ModelViewSet):
    queryset = SaleBicycle.objects.all()
    serializer_class = SaleBicycleSerializer

class EquipmentView(viewsets.ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer

class RentEquipmentView(viewsets.ModelViewSet):
    queryset = RentEquipment.objects.all()
    serializer_class = RentEquipmentSerializer

class SaleEquipmentView(viewsets.ModelViewSet):
    queryset = SaleEquipment.objects.all()
    serializer_class = SaleEquipmentSerializer

class ReservationView(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class ReservationRentView(viewsets.ModelViewSet):
    queryset = ReservationRent.objects.all()
    serializer_class = ReservationRentSerializer

class ReservationSaleView(viewsets.ModelViewSet):
    queryset = ReservationSale.objects.all()
    serializer_class = ReservationSaleSerializer
