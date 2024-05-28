"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api import views
from rest_framework_simplejwt import views as jwt_views

router = routers.DefaultRouter()
router.register(r'products', views.ProductView, 'product')
router.register(r'category', views.CategoryView, 'category')
router.register(r'bicycles', views.BicycleView, 'bicycle')
router.register(r'rentBicycles', views.RentBicycleView, 'rentBicycle')
router.register(r'saleBicycles', views.SaleBicycleView, 'saleBicycle')
router.register(r'equipment', views.EquipmentView, 'equipment')
router.register(r'rentEquipment', views.RentEquipmentView, 'rentEquipment')
router.register(r'saleEquipment', views.SaleEquipmentView, 'saleEquipment')
router.register(r'reservation', views.ReservationView, 'reservation')
router.register(r'rentReservation', views.ReservationRentView, 'rentReservation')
router.register(r'saleReservation', views.ReservationSaleView, 'saleReservation')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('token/', 
          jwt_views.TokenObtainPairView.as_view(), 
          name ='token_obtain_pair'),
    path('token/refresh/', 
          jwt_views.TokenRefreshView.as_view(), 
          name ='token_refresh'),
    path('', include('authentification.urls')),

]
