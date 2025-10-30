from django.urls import path
from .views import userData

urlpatterns = [
    path('userData',userData,name='userdata'),
]