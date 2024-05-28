from django.contrib import admin
from .models import Product, Category, Bicycle, RentBicycle, SaleBicycle, Equipment, RentEquipment, SaleEquipment, Reservation, ReservationRent, ReservationSale

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand')

admin.site.register(Product, ProductAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(Category, CategoryAdmin)

class BicycleAdmin(ProductAdmin):
    list_display = ('id', 'brand', 'model', 'category')

admin.site.register(Bicycle, BicycleAdmin)

class RentBicycleAdmin(BicycleAdmin):
    list_display = ('id', 'brand', 'model', 'category', 'reservedDates', 'pricePerDay')

admin.site.register(RentBicycle, RentBicycleAdmin)

class SaleBicycleAdmin(BicycleAdmin):
    list_display = ('id', 'brand', 'model', 'category', 'price', 'availability')

admin.site.register(SaleBicycle, SaleBicycleAdmin)

class EquipmentAdmin(ProductAdmin):
    list_display = ('id', 'brand', 'model', 'name')

admin.site.register(Equipment, EquipmentAdmin)

class RentEquipmentAdmin(EquipmentAdmin):
    list_display = ('id', 'brand', 'model', 'name', 'reservedDates', 'pricePerDay')

admin.site.register(RentEquipment, RentEquipmentAdmin)

class SaleEquipmentAdmin(EquipmentAdmin):
    list_display = ('id', 'brand', 'model', 'name', 'price', 'availability' )

admin.site.register(SaleEquipment, SaleEquipmentAdmin)

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('oib', 'date')
    filter_horizontal = ('products',)

admin.site.register(Reservation)

class ReservationRentAdmin(ReservationAdmin):
    list_display = ('oib', 'date', 'reservedDates')
    filter_horizontal = ('products',)

admin.site.register(ReservationRent)

class ReservationSaleAdmin(ReservationAdmin):
    list_display = ('oib', 'date', 'dateToCollect')
    filter_horizontal = ('products',)

admin.site.register(ReservationSale)
