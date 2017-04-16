countries = {
    'Thailand': {'sea': True, 'schengen': False, 'average_temperature': 30, 'currency_rate': 1.8, 'day_price': 111},
    'Hungary': {'sea': False, 'schengen': True, 'average_temperature': 10, 'currency_rate': 0.3, 'day_price': 800},
    'Germany': {'sea': True, 'schengen': True, 'average_temperature': 5, 'currency_rate': 20, 'day_price': 15},
    'Japan': {'sea': True, 'schengen': False, 'average_temperature': 15, 'currency_rate': 0.61, 'day_price': 200},
    'Poland': {'sea': False, 'schengen': True, 'average_temperature': 7, 'currency_rate': 0.1, 'day_price': 1000},
    'Spain': {'sea': True, 'schengen': True, 'average_temperature': 20, 'currency_rate': 2, 'day_price': 95},
    'Russia': {'sea': True, 'schengen': False, 'average_temperature': -6, 'currency_rate': 0.08, 'day_price': 2000},
    'Greek': {'sea': True, 'schengen': True, 'average_temperature': 21, 'currency_rate': 0.1, 'day_price': 1200},
    'Afghanistan': {'sea': False, 'schengen': False, 'average_temperature': 32, 'currency_rate': 0.01, 'day_price': 999}
}

schengen_countries = set()
sea_countries = set()

for country_name, propertys in countries.items():
    if propertys['schengen']:
        schengen_countries.add(country_name)
    if propertys['sea']:
        sea_countries.add(country_name)

print('Страны с морем:', sea_countries)
print('Страны в шенгене:', schengen_countries)
print('Страны в шенгене с морем:', schengen_countries & sea_countries)
print('Страны в шенгене или с морем:', schengen_countries | sea_countries)

money_amount = 5000
for country_name, propertys in countries.items():
    print('В', country_name, 'у нас будет %.2f денег в местной валюте' % (money_amount / propertys['currency_rate']))

sea_schengen_countries = schengen_countries & sea_countries

for country_name in sea_schengen_countries:
    print(country_name, countries[country_name])

super_countries = set()

for country_name, propertys in countries.items():
    if (propertys['sea']) and (propertys['average_temperature'] > 17 or propertys['schengen']) and (propertys['day_price']*30 < money_amount/propertys['currency_rate']):
        super_countries.add(country_name)

print(super_countries)
