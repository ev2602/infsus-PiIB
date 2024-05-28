from django.test import SimpleTestCase
from django.urls import reverse, resolve
from rest_framework.test import APIRequestFactory
from api import views

class TestUrls(SimpleTestCase):

    def test_product_url_is_resolved(self):
        url = reverse('product-list')
        self.assertEqual(resolve(url).func.cls, views.ProductView)

    def test_category_url_is_resolved(self):
        url = reverse('category-list')
        self.assertEqual(resolve(url).func.cls, views.CategoryView)

    def test_bicycle_url_is_resolved(self):
        url = reverse('bicycle-list')
        self.assertEqual(resolve(url).func.cls, views.BicycleView)

    def test_rentBicycle_url_is_resolved(self):
        url = reverse('rentBicycle-list')
        self.assertEqual(resolve(url).func.cls, views.RentBicycleView)

    def test_saleBicycle_url_is_resolved(self):
        url = reverse('saleBicycle-list')
        self.assertEqual(resolve(url).func.cls, views.SaleBicycleView)

    def test_equipment_url_is_resolved(self):
        url = reverse('equipment-list')
        self.assertEqual(resolve(url).func.cls, views.EquipmentView)

    def test_rentEquipment_url_is_resolved(self):
        url = reverse('rentEquipment-list')
        self.assertEqual(resolve(url).func.cls, views.RentEquipmentView)

    def test_saleEquipment_url_is_resolved(self):
        url = reverse('saleEquipment-list')
        self.assertEqual(resolve(url).func.cls, views.SaleEquipmentView)

    def test_reservation_url_is_resolved(self):
        url = reverse('reservation-list')
        self.assertEqual(resolve(url).func.cls, views.ReservationView)

    def test_rentReservation_url_is_resolved(self):
        url = reverse('rentReservation-list')
        self.assertEqual(resolve(url).func.cls, views.ReservationRentView)

    def test_saleReservation_url_is_resolved(self):
        url = reverse('saleReservation-list')
        self.assertEqual(resolve(url).func.cls, views.ReservationSaleView)
