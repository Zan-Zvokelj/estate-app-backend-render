from django.urls import include, path
from ESTATE_APP_BACKEND.properties import views
from ESTATE_APP_BACKEND.properties.views import PropertyViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'properties', views.PropertyViewSet)   # Register the view in the router


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('properties-sale/', views.PropertiesSaleViewSet.as_view(), name='properties-sale'),
    path('properties-home/', views.PropertiesHomeViewSet.as_view(), name='properties-home'),
    path('properties-parking/', views.PropertiesParkingViewSet.as_view(), name='properties-parking'),
]