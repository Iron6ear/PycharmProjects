#Декомпозиция - разбиение целого на части
temperature = []
with open('temperature.txt', 'rt') as t:
    for line in t:
        temperature.append(int(line))

avg = sum(temperature)/len(temperature)

print('Средняя температура: {0}'.format(avg))
