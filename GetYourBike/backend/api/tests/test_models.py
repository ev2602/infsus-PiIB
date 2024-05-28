from django.test import TestCase
from django.contrib.postgres.fields import ArrayField
from api.models import Product, Category, Bicycle, RentBicycle, SaleBicycle, Equipment, RentEquipment, SaleEquipment, Reservation, ReservationRent, ReservationSale

class TestProductModel(TestCase):

    def setUp(self):
        self.product = Product.objects.create(brand='Brand A')

    def test_product_creation(self):
        self.assertIsInstance(self.product, Product)
        self.assertEqual(self.product.brand, 'Brand A')


class TestCategoryModel(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name='Category A')

    def test_category_creation(self):
        self.assertIsInstance(self.category, Category)
        self.assertEqual(self.category.name, 'Category A')


class TestBicycleModel(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name='Category A')
        self.bicycle = Bicycle.objects.create(brand='Brand B', model='Model X', category=self.category)

    def test_bicycle_creation(self):
        self.assertIsInstance(self.bicycle, Bicycle)
        self.assertEqual(self.bicycle.brand, 'Brand B')
        self.assertEqual(self.bicycle.model, 'Model X')
        self.assertEqual(self.bicycle.category, self.category)


class TestRentBicycleModel(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name='Category A')
        self.rent_bicycle = RentBicycle.objects.create(
            brand='Brand C', model='Model Y', category=self.category,
            reservedDates=['2024-06-01', '2024-06-02'], pricePerDay=20.0
        )

    def test_rent_bicycle_creation(self):
        self.assertIsInstance(self.rent_bicycle, RentBicycle)
        self.assertEqual(self.rent_bicycle.brand, 'Brand C')
        self.assertEqual(self.rent_bicycle.model, 'Model Y')
        self.assertEqual(self.rent_bicycle.category, self.category)
        self.assertEqual(self.rent_bicycle.reservedDates, ['2024-06-01', '2024-06-02'])
        self.assertEqual(self.rent_bicycle.pricePerDay, 20.0)


class TestSaleBicycleModel(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name='Category A')
        self.sale_bicycle = SaleBicycle.objects.create(
            brand='Brand D', model='Model Z', category=self.category,
            price=500.0, availability=10
        )

    def test_sale_bicycle_creation(self):
        self.assertIsInstance(self.sale_bicycle, SaleBicycle)
        self.assertEqual(self.sale_bicycle.brand, 'Brand D')
        self.assertEqual(self.sale_bicycle.model, 'Model Z')
        self.assertEqual(self.sale_bicycle.category, self.category)
        self.assertEqual(self.sale_bicycle.price, 500.0)
        self.assertEqual(self.sale_bicycle.availability, 10)


class TestEquipmentModel(TestCase):

    def setUp(self):
        self.equipment = Equipment.objects.create(brand='Brand E', name='Equipment A')

    def test_equipment_creation(self):
        self.assertIsInstance(self.equipment, Equipment)
        self.assertEqual(self.equipment.brand, 'Brand E')
        self.assertEqual(self.equipment.name, 'Equipment A')


class TestRentEquipmentModel(TestCase):

    def setUp(self):
        self.rent_equipment = RentEquipment.objects.create(
            brand='Brand F', name='Equipment B',
            reservedDates=['2024-06-01', '2024-06-02'], pricePerDay=15.0
        )

    def test_rent_equipment_creation(self):
        self.assertIsInstance(self.rent_equipment, RentEquipment)
        self.assertEqual(self.rent_equipment.brand, 'Brand F')
        self.assertEqual(self.rent_equipment.name, 'Equipment B')
        self.assertEqual(self.rent_equipment.reservedDates, ['2024-06-01', '2024-06-02'])
        self.assertEqual(self.rent_equipment.pricePerDay, 15.0)


class TestSaleEquipmentModel(TestCase):

    def setUp(self):
        self.sale_equipment = SaleEquipment.objects.create(
            brand='Brand G', name='Equipment C',
            price=100.0, availability=5
        )

    def test_sale_equipment_creation(self):
        self.assertIsInstance(self.sale_equipment, SaleEquipment)
        self.assertEqual(self.sale_equipment.brand, 'Brand G')
        self.assertEqual(self.sale_equipment.name, 'Equipment C')
        self.assertEqual(self.sale_equipment.price, 100.0)
        self.assertEqual(self.sale_equipment.availability, 5)


class TestReservationModel(TestCase):

    def setUp(self):
        self.product1 = Product.objects.create(brand='Brand H')
        self.product2 = Product.objects.create(brand='Brand I')
        self.reservation = Reservation.objects.create(
            oib='123456789', date='2024-06-01'
        )
        self.reservation.products.set([self.product1, self.product2])

    def test_reservation_creation(self):
        self.assertIsInstance(self.reservation, Reservation)
        self.assertEqual(self.reservation.oib, '123456789')
        self.assertEqual(self.reservation.date, '2024-06-01')
        self.assertEqual(list(self.reservation.products.all()), [self.product1, self.product2])


class TestReservationRentModel(TestCase):

    def setUp(self):
        self.product1 = Product.objects.create(brand='Brand J')
        self.product2 = Product.objects.create(brand='Brand K')
        self.reservation_rent = ReservationRent.objects.create(
            oib='987654321', date='2024-07-01',
            reservedDates=['2024-07-10', '2024-07-11']
        )
        self.reservation_rent.products.set([self.product1, self.product2])

    def test_reservation_rent_creation(self):
        self.assertIsInstance(self.reservation_rent, ReservationRent)
        self.assertEqual(self.reservation_rent.oib, '987654321')
        self.assertEqual(self.reservation_rent.date, '2024-07-01')
        self.assertEqual(self.reservation_rent.reservedDates, ['2024-07-10', '2024-07-11'])
        self.assertEqual(list(self.reservation_rent.products.all()), [self.product1, self.product2])


class TestReservationSaleModel(TestCase):

    def setUp(self):
        self.product1 = Product.objects.create(brand='Brand L')
        self.product2 = Product.objects.create(brand='Brand M')
        self.reservation_sale = ReservationSale.objects.create(
            oib='123123123', date='2024-08-01',
            dateToCollect='2024-08-05'
        )
        self.reservation_sale.products.set([self.product1, self.product2])

    def test_reservation_sale_creation(self):
        self.assertIsInstance(self.reservation_sale, ReservationSale)
        self.assertEqual(self.reservation_sale.oib, '123123123')
        self.assertEqual(self.reservation_sale.date, '2024-08-01')
        self.assertEqual(self.reservation_sale.dateToCollect, '2024-08-05')
        self.assertEqual(list(self.reservation_sale.products.all()), [self.product1, self.product2])
