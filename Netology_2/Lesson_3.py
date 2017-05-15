# __file__ содержит реальное расположение скрипта

import os.path
import codecs

local_path = os.path.dirname(os.path.realpath(__file__))
countries_path = os.path.join(local_path, 'countries.txt')

print(countries_path)

with codecs.open(countries_path, encoding='UTF-8') as countries:
    for country in countries:
        print(country.strip())
