from django.urls import path
from .views import about, medicine

urlpatterns = [
    path('about/', about, name='users-view'),
    path('medicine/', medicine, name='product-medicines'),
]