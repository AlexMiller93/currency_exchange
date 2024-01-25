from django.urls import path
from .views import GetUSDView, delete_rates

urlpatterns = [
    path('get-current-usd/', GetUSDView.as_view(), name='get_usd'),
    path('delete-rates/', delete_rates, name='delete_rates'),
]