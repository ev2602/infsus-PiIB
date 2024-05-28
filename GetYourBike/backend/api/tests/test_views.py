from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from api.models import Product, Category, Bicycle, RentBicycle, SaleBicycle, Equipment, RentEquipment, SaleEquipment, Reservation, ReservationRent, ReservationSale
from api.serializers import ProductSerializer, CategorySerializer, BicycleSerializer, RentBicycleSerializer, SaleBicycleSerializer, EquipmentSerializer, RentEquipmentSerializer, SaleEquipmentSerializer, ReservationSerializer, ReservationRentSerializer, ReservationSaleSerializer


class TestViews(TestCase):
    
    def setUp(self):
        self.client = APIClient()
        self.product = Product.objects.create(brand='Test Brand')
        self.category = Category.objects.create(name='Test Category')
        self.bicycle = Bicycle.objects.create(brand='Giant', model='XTC', category=self.category)
        self.rent_bicycle = RentBicycle.objects.create(
            brand='Giant',
            model='XTC',
            category=self.category,
            reservedDates=['2024-05-29', '2024-05-30'],
            pricePerDay=20.0
        )
        self.valid_payload_rentbicycle = {
            'brand': 'Trek',
            'model': 'Marlin 5',
            'category': self.category.id,
            'reservedDates': ['2024-02-01', '2024-02-02'],
            'pricePerDay': 25.0
        }
        self.invalid_payload_rentbicylce = {
            'brand': '',
            'model': 'Marlin 5',
            'category': self.category.id,
            'reservedDates': ['2024-02-01', '2024-02-02'],
            'pricePerDay': 25.0
        }
        self.equipment = Equipment.objects.create(name='Helmet')
        self.rent_equipment = RentEquipment.objects.create(
            brand='Test',
            name='Helmet',
            reservedDates=['2024-01-01', '2024-01-02'],
            pricePerDay=15.0
        )
        self.valid_payload_renteqipment = {
            'brand': 'Test',
            'name': 'Goggles',
            'reservedDates': ['2024-02-01', '2024-02-02'],
            'pricePerDay': 10.0
        }
        self.invalid_payload_rentequipment = {
            'brand': 'Test',
            'name': '',
            'reservedDates': ['2024-02-01', '2024-02-02'],
            'pricePerDay': 10.0
        }
        self.product1 = Product.objects.create(brand='Brand A')
        self.product2 = Product.objects.create(brand='Brand B')
        self.reservation_rent = ReservationRent.objects.create(
            oib='123456789',
            date='2024-06-01',
            reservedDates=['2024-06-10', '2024-06-11']
        )
        self.reservation_rent.products.set([self.product1, self.product2])

        self.valid_payload_reservationrent = {
            'oib': '987654321',
            'date': '2024-07-01',
            'reservedDates': ['2024-07-10', '2024-07-11'],
            'products': [self.product1.id, self.product2.id]
        }
        self.invalid_payload_reservationrent = {
            'oib': '',
            'date': '2024-07-01',
            'reservedDates': ['2024-07-10', '2024-07-11'],
            'products': [self.product1.id, self.product2.id]
        }

    def test_products_GET(self):
        response = self.client.get(reverse('product-list'))
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_category_GET(self):
        response = self.client.get(reverse('category-list'))
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_bicycle_GET(self):
        response = self.client.get(reverse('bicycle-list'))
        bicycles = Bicycle.objects.all()
        serializer = BicycleSerializer(bicycles, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_rent_bicycles_GET(self):
        response = self.client.get(reverse('rentBicycle-list'))
        rent_bicycles = RentBicycle.objects.all()
        serializer = RentBicycleSerializer(rent_bicycles, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_rent_bicycle_single_GET(self):
        response = self.client.get(reverse('rentBicycle-detail', kwargs={'pk': self.rent_bicycle.pk}))
        rent_bicycle = RentBicycle.objects.get(pk=self.rent_bicycle.pk)
        serializer = RentBicycleSerializer(rent_bicycle)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_rent_bicycle_CREATE(self):
        response = self.client.post(reverse('rentBicycle-list'), self.valid_payload_rentbicycle)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(RentBicycle.objects.count(), 2)
        self.assertEqual(RentBicycle.objects.get(pk=response.data['id']).brand, 'Trek')

    def test_invalid_rent_bicycle_CREATE(self):
        response = self.client.post(reverse('rentBicycle-list'), self.invalid_payload_rentbicylce)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_rent_bicycle_UPDATE(self):
        response = self.client.put(reverse('rentBicycle-detail', kwargs={'pk': self.rent_bicycle.pk}), self.valid_payload_rentbicycle)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.rent_bicycle.refresh_from_db()
        self.assertEqual(self.rent_bicycle.brand, 'Trek')

    def test_rent_bicycle_DELETE(self):
        response = self.client.delete(reverse('rentBicycle-detail', kwargs={'pk': self.rent_bicycle.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(RentBicycle.objects.count(), 0)

    def test_rent_equipment_GET(self):
        response = self.client.get(reverse('rentEquipment-list'))
        rent_equipment = RentEquipment.objects.all()
        serializer = RentEquipmentSerializer(rent_equipment, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_rent_equipment_single_GET(self):
        response = self.client.get(reverse('rentEquipment-detail', kwargs={'pk': self.rent_equipment.pk}))
        rent_equipment = RentEquipment.objects.get(pk=self.rent_equipment.pk)
        serializer = RentEquipmentSerializer(rent_equipment)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_rent_equipment_CREATE(self):
        response = self.client.post(reverse('rentEquipment-list'), self.valid_payload_renteqipment)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(RentEquipment.objects.count(), 2)
        self.assertEqual(RentEquipment.objects.get(pk=response.data['id']).name, 'Goggles')

    def test_invalid_rent_equipment_CREATE(self):
        response = self.client.post(reverse('rentEquipment-list'), self.invalid_payload_rentequipment)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_rent_equipment_UPDATE(self):
        response = self.client.put(reverse('rentEquipment-detail', kwargs={'pk': self.rent_equipment.pk}), self.valid_payload_renteqipment)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.rent_equipment.refresh_from_db()
        self.assertEqual(self.rent_equipment.name, 'Goggles')

    def test_rent_equipment_DELETE(self):
        response = self.client.delete(reverse('rentEquipment-detail', kwargs={'pk': self.rent_equipment.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(RentEquipment.objects.count(), 0)

    def test_get_all_reservation_rents(self):
        response = self.client.get(reverse('rentReservation-list'))
        reservation_rents = ReservationRent.objects.all()
        serializer = ReservationRentSerializer(reservation_rents, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_single_reservation_rent(self):
        response = self.client.get(reverse('rentReservation-detail', kwargs={'pk': self.reservation_rent.pk}))
        reservation_rent = ReservationRent.objects.get(pk=self.reservation_rent.pk)
        serializer = ReservationRentSerializer(reservation_rent)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_reservation_rent(self):
        response = self.client.post(reverse('rentReservation-list'), self.valid_payload_reservationrent)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ReservationRent.objects.count(), 2)

    def test_create_invalid_reservation_rent(self):
        response = self.client.post(reverse('rentReservation-list'), self.invalid_payload_reservationrent)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_reservation_rent(self):
        response = self.client.put(reverse('rentReservation-detail', kwargs={'pk': self.reservation_rent.pk}), self.valid_payload_reservationrent)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.reservation_rent.refresh_from_db()
        self.assertEqual(self.reservation_rent.oib, '987654321')

    def test_delete_reservation_rent(self):
        response = self.client.delete(reverse('rentReservation-detail', kwargs={'pk': self.reservation_rent.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(ReservationRent.objects.count(), 0)