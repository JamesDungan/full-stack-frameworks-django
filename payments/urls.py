from django.urls import path

from .views import payments, charge

urlpatterns = [
    path('', payments, name='payments'),
    path('charge/', charge, name='charge'),
]