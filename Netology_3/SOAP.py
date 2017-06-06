#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# http://www.webservicex.net/new/Home/Index
# https://bitbucket.org/sboz/osa/wiki/Home
# https://fedoraproject.org/wiki/Infrastructure/Fedorahosted-retirement


import osa

URL = 'http://www.webservicex.net/ConvertTemperature.asmx?WSDL'
client = osa.client.Client(URL)
print(client.types)
response = client.service.ConvertTemp(Temperature=15.00, FromUnit='degreeFahrenheit', ToUnit='degreeCelsius')

print(response)
