# Декомпозиция - разбиение целого на части
# .strip() - удаление пробельных символов или других символов
# .split() - разделение строки и привращение в список
# .extend() - соединение списков

from pprint import pprint

temperature = []
with open('temperature.txt') as t:
    for line in t:
        temperature.append(int(line))

avg = sum(temperature)/len(temperature)

print('Средняя температура: {0}'.format(avg))

with open('average_temperature.txt', 'w') as average_temperature:
    average_temperature.write(str(avg))

cities = dict()

with open('week_temperature.txt') as f_week_temperature:
    for city in f_week_temperature:
        temperatures = f_week_temperature.readline()
        cities[city.strip()] = temperatures.split()

pprint(cities)

for city, temperatures in cities.items():
    avg = 0
    for t in temperatures:
        avg += int(t)
    avg = avg / len(temperatures)
    print(city, '%.2f' % avg)
