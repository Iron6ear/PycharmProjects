residence_limit = 90
schengen_constraint = 180
visits = [[1, 10], [61, 90], [101, 140], [141, 160], [164, 172], [175, 185]]
control_day = 12

for visit in visits:
    if not isinstance(visit, list) or visit[0] > visit[1]:
        raise Exception('Ошибка в данных поездки ', visit)
    elif visit[0] > schengen_constraint:
        raise Exception('Начало этой поездки выходит интервал Шенгенской визы', visit)

days_for_visits = []
total_time_in_es = 0
date_of_departures = 0
for visit in visits:
    days_for_visit = 0
    for past_visit in visits:
        if past_visit[0] < visit[0] and visit[1] <= schengen_constraint:
            days_for_visit += past_visit[1] - past_visit[0] + 1
    if date_of_departures > visit[0]:
        raise Exception('Ошибка с датами пресечения границы в поездке', visit, 'или предыдущей')
    date_of_departures = visit[1]

    days_for_visit += visit[1] - visit[0] + 1
    days_for_visits.append(days_for_visit)

print(days_for_visits)
assert (days_for_visits == [10, 40, 80, 100, 109, 11])

i = 0
control_period = []
while i < len(visits):
    if visits[i][0] <= control_day <= visits[i][1]:
        print('Эта дата входит в существующий интервал', visits[i])
        control_period.append(visits[i])
    i += 1

if not control_period:
    period = 0
    for day_d in visits:
        if day_d[0] > control_day:
            break
        else:
            period = day_d
    print('У Вас осталось', schengen_constraint - days_for_visits[visits.index(period)], 'дней в этом периоде визы.')
else:
    print('Неверно задана дата')

for visit, total_days in zip(visits, days_for_visits):
    if total_days > residence_limit:
        overstay_time = total_days - residence_limit
        print('Во время визита', visit, 'количество время пребывания превышено на', overstay_time, 'дней')
