from rest_framework import serializers
from .models import Product, Category, Bicycle, RentBicycle, SaleBicycle, Equipment, SaleEquipment, RentEquipment, Reservation, ReservationRent, ReservationSale

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'brand')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')

class BicycleSerializer(ProductSerializer):
    class Meta(ProductSerializer.Meta):
        model = Bicycle
        fields =  ProductSerializer.Meta.fields + ('model', 'category')

class RentBicycleSerializer(BicycleSerializer):
    class Meta(BicycleSerializer.Meta):
        model = RentBicycle
        fields = BicycleSerializer.Meta.fields + ('reservedDates', 'pricePerDay')

class SaleBicycleSerializer(BicycleSerializer):
    class Meta(BicycleSerializer.Meta):
        model = SaleBicycle
        fields = BicycleSerializer.Meta.fields + ('price', 'availability')

class EquipmentSerializer(ProductSerializer):
    class Meta(ProductSerializer.Meta):
        model = Equipment
        fields =  ProductSerializer.Meta.fields + ('name',)

class RentEquipmentSerializer(EquipmentSerializer):
    class Meta(EquipmentSerializer.Meta):
        model = RentEquipment
        fields =  EquipmentSerializer.Meta.fields + ('reservedDates', 'pricePerDay')

class SaleEquipmentSerializer(EquipmentSerializer):
    class Meta(EquipmentSerializer.Meta):
        model = SaleEquipment
        fields =  EquipmentSerializer.Meta.fields + ('price', 'availability')

class ReservationSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Reservation
        fields = ('id', 'oib', 'date', 'products')

    def create(self, validated_data):
        products_data = validated_data.pop('products')
        reservation = Reservation.objects.create(**validated_data)
        for product_data in products_data:
            product, created = Product.objects.get_or_create(**product_data)
            reservation.products.add(product)
        return reservation

    def update(self, instance, validated_data):
        products_data = validated_data.pop('products')
        instance.oib = validated_data.get('oib', instance.oib)
        instance.date = validated_data.get('date', instance.date)
        instance.save()

        instance.products.clear()
        for product_data in products_data:
            product, created = Product.objects.get_or_create(**product_data)
            instance.products.add(product)

        return instance

class ReservationRentSerializer(ReservationSerializer):
    class Meta(ReservationSerializer):
        model = ReservationRent
        fields = ReservationSerializer.Meta.fields + ('reservedDates',)

class ReservationSaleSerializer(ReservationSerializer):
    class Meta(ReservationSerializer):
        model = ReservationSale
        fields = ReservationSerializer.Meta.fields + ('dateToCollect',)
