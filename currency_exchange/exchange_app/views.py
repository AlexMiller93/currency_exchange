import time
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import redirect
from django.views import View
import requests

from .models import ExchangeRequest

BASE_URL = 'http://data.fixer.io/api/'

# Create your views here.
class GetUSDView(View):
    def get(self, request, *args, **kwargs):
        # Запрос курса доллара к рублю
        usd_to_rub_rate, date = self.fetch_usd_to_rub_rate()

        # Сохранение запроса в истории
        ExchangeRequest.objects.create(usd_to_rub_rate=usd_to_rub_rate, timestamp=date)

        # Получение последних 10 запросов
        latest_requests = self.get_latest_requests()

        # Добавление паузы между запросами (10 секунд)
        time.sleep(10)
        
        # Отправка JSON-ответа
        return JsonResponse({
            'usd_to_rub_rate': usd_to_rub_rate,
            'latest_requests': latest_requests,
        })

    def fetch_usd_to_rub_rate(self):
        # Запрос на получение информации по курсу доллара к рублю
        url = f"{BASE_URL}latest?access_key={settings.API_KEY}&symbols=USD,RUB&format=1"
        data = requests.get(url).json()
        if data["success"]:
            rates = data["rates"]
            exchange_rate = round(rates["RUB"] / rates["USD"], 3)
            exchange_date = data["date"]
            return exchange_rate, exchange_date

    def get_latest_requests(self):
        # Получение последних 10 запросов
        return list(ExchangeRequest.objects.values('timestamp', 'usd_to_rub_rate')[1:11])
    

def delete_rates(request):
    rates_to_delete = ExchangeRequest.objects.all()
    rates_to_delete.delete()
    return redirect('get_usd')