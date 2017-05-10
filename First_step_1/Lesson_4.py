import csv
countries = dict()

with open('countries.csv') as csv_file:
    reader = csv.DictReader(csv_file, delimiter=';')
    for row in reader:
        countries[row['name']] = {'sea': bool(row['sea']),
                                  'schengen': bool(row['schengen']),
                                  'average_temperature': float(row['average_temperature']),
                                  'currency_rate': float(row['currency_rate']),
                                  'day_price': float(row['day_price'])}

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
    if (propertys['sea']) \
            and (propertys['average_temperature'] > 17 or propertys['schengen'])\
            and (propertys['day_price']*30 < money_amount/propertys['currency_rate']):
        super_countries.add(country_name)

print(super_countries)
