# Сделать интерактивное приложение
# Ждёт от вас ввод, строку
#    v - просит ввести новый визит (начало, затем конец)
#        ошибка ввода если:
#            Дата отъезна меньше даты приезда
#            Дата приезна входит в прошлый визит
#            Введены не числа
#    p - просит ввести дату следующего визита, говорит, сколько дней вы можете провести в шенгене
#    r - просит ввести начало и конец визита, удаляет визит
#    e - выход
# Выводит текущий список визитов
# Вывод сообщение о нарушения условий пребывания:
#    Если вы превысили 90 дневный лимит за 180 дневный срок
#    Если дата прибытия выходит за 180 дневный срок пребывания, но входит в 90 дневный лимит
# Ожидается, что повторяющиеся или громоздкий код вы попробуете вынести в функции


RESIDENCE_LIMIT = 90
SCHENGEN_CONSTRAINT = 180
visits = list()


def total_days_in_eu(list_of_visit):
    summ_of_days = 0
    for visit in list_of_visit:
        summ_of_days += visit[1] - visit[0] + 1
    return summ_of_days


def input_visit():
    start_visit_date = int(input('Введите начало визита: '))
    end_visit_date = int(input('Введите конец визита: '))
    this_visit = list()
    this_visit.append(start_visit_date)
    this_visit.append(end_visit_date)
    return this_visit


while True:
    input_argument = input('Если не знает, что ввести, введите \"h\": ')
    if input_argument == 'h':
        print('    v - просит ввести новый визит (начало, затем конец) \n'
              '    l - просит ввести дату следующего визита, говорит, сколько дней вы можете провести в шенгене\n'
              '    r - просит ввести начало и конец визита, удаляет визит\n'
              '    p - выводит текущий список визитов\n'
              '    h - помощь\n'
              '    e - выход\n')
    elif input_argument == 'e':
        print('Выход')
        break
    elif input_argument == 'v':
        visits.append(input_visit())
    elif input_argument == 'p':
        print(visits)
    elif input_argument == 'r':
        visits.remove(input_visit())
    elif input_argument == 'l':
        next_visit = int(input('Введите начало следующего визита: '))
        last_residence_limit = RESIDENCE_LIMIT - total_days_in_eu(visits)
        last_schengen_constraint = SCHENGEN_CONSTRAINT - next_visit
        if last_residence_limit > last_schengen_constraint:
            print('Вы можете провести в EU {0} дней'.format(last_schengen_constraint))
        else:
            print('Вы можете провести в EU {0} дней'.format(last_residence_limit))
