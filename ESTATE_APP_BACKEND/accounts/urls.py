from django.urls import path
from .views import UserRegistrationView, CustomAuthToken

urlpatterns = [
    path('api/register/', UserRegistrationView.as_view(), name='register'),
    path('api/auth/', CustomAuthToken.as_view(), name='login'),
]
