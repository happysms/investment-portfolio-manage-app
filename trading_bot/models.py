from django.conf import settings
from django.db import models


class TradingRecord(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    time = models.DateTimeField()
    symbol = models.CharField(max_length=20)
    side = models.CharField(max_length=20)
    price = models.FloatField()
    quantity = models.FloatField()
    Fee = models.FloatField()

    profit = models.FloatField()

    def __str__(self):
        return f"{self.time} / {self.side} {self.price}"



