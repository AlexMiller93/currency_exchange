from django.db import models

# Create your models here.
class ExchangeRequest(models.Model):
    timestamp = models.DateField(auto_now=True)
    usd_to_rub_rate = models.FloatField()
    