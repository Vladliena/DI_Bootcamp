"""
URL configuration for bike_store project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from rent.views import RentalView, CustomerView, VehicleView, RentalStationView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('rent/rental/', RentalView.as_view(), name='rental-list'),
    path('rent/rental/<int:pk>/', RentalView.as_view(), name='rental-detail'),
    path('rent/customer/', CustomerView.as_view(), name='customer-list'),
    path('rent/customer/add/', CustomerView.as_view(), {'action': 'add'},  name='customer-add'),
    path('rent/vehicle/', VehicleView.as_view(), name='vehicle-list'),
    path('rent/vehicle/add/', VehicleView.as_view(), {'action': 'add'}, name='vehicle-add'),
    path('rent/vehicle/<int:pk>/', VehicleView.as_view(), name='vehicle-detail'),
    path('rent/station/', RentalStationView.as_view(), name='station-list'),
    path('rent/station/add/', RentalStationView.as_view(), {'action': 'add'}, name='station-add'),
    path('rent/station/<int:pk>/', RentalStationView.as_view(), name='station-detail'),
    # path('rent/station/distribution/', RentalStationView.as_view(), {'action': 'distribution'}, name='station-distribution'),
    # path('rent/station/distribute/', RentalStationView.as_view(), {'action': 'distribute'}, name='station-distribute'),
]
