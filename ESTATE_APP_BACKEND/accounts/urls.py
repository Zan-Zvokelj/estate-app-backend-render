from accounts import views
from django.urls import path

urlpatterns = [
    path('api/auth/', views.CustomAuthToken.as_view()),
    path('api/register/', views.UserRegistrationView.as_view(), name='user-registration') 
]