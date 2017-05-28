#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# https://fx.currencysystem.com/webservices/CurrencyServer5.asmx

import osa

URL = 'http://fx.currencysystem.com/webservices/CurrencyServer5.asmx?WSDL'
client = osa.client.Client(URL)

response = client.service.AllCurrencies()

print(response)
response2 = client.service.Convert(fromCurrency='EUR', toCurrency='RUB', amount=100, rounding=False)
print(response2)
