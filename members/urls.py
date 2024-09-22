from django.urls import path
from .views import custom_login, custom_logout, signup


urlpatterns = [
    path('register/', signup, name='register'),
    path('login/', custom_login, name='login'),
    path('logout/',custom_logout, name='logout'),
]

