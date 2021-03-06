# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Cryptocurrency(models.Model):
    tag = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length = 200, null=True)
    symbol = models.CharField(max_length = 200, null=True)
    rank = models.IntegerField(null=True)
    price_usd = models.DecimalField(max_digits = 200, decimal_places = 2, null=True)
    price_btc = models.DecimalField(max_digits = 200, decimal_places = 10, null=True)
    volume_24h_usd = models.DecimalField(max_digits = 200, decimal_places = 2, null=True)
    market_cap_usd = models.DecimalField(max_digits = 200, decimal_places = 2, null=True)
    available_supply = models.DecimalField(max_digits = 200, decimal_places = 2, null=True)
    total_supply = models.DecimalField(max_digits = 200, decimal_places = 2, null=True)
    percent_change_1h = models.DecimalField(max_digits = 200, decimal_places = 2, null=True)
    percent_change_24h = models.DecimalField(max_digits = 200, decimal_places = 2, null=True)
    percent_change_7d = models.DecimalField(max_digits = 200, decimal_places = 2, null=True)
    last_updated = models.IntegerField(null = True)

    def __str__(self):
        return self.tag
