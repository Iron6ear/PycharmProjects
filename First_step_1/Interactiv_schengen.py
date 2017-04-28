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
    try:
        start_visit_date = int(input('Введите начало визита: '))
    except ValueError:
        print('Неправильно введенные данные начала визита.')
        start_visit_date = None
    try:
        end_visit_date = int(input('Введите конец визита: '))
    except ValueError:
        print('Неправильно введенные данные конца визита.')
        end_visit_date = None
    this_visit = list()
    try:
        if end_visit_date < start_visit_date:
            this_visit = [None, None]
            print('Дата начала визита позже даты конца визита.')
        elif start_visit_date < visits[-1][-1] and end_visit_date != visits[-1][-1]:
            this_visit = [None, None]
            print('Дата начала визита пересекается с предыдущим визитом.')
        else:
            this_visit.append(start_visit_date)
            this_visit.append(end_visit_date)
    except IndexError:
        this_visit.append(start_visit_date)
        this_visit.append(end_visit_date)
    return this_visit


while True:
    input_argument = input('Если не знает, что ввести, введите \"h\": ')
    if input_argument == 'h':
        print('    v - просит ввести новый визит (начало, затем конец)\n'
              '    d - загружает данные о визитах из файла\n'
              '    l - просит ввести дату следующего визита, говорит, сколько дней вы можете провести в шенгене\n'
              '    r - просит ввести начало и конец визита, удаляет визит\n'
              '    p - выводит текущий список визитов\n'
              '    h - помощь\n'
              '    e - выход\n')
    elif input_argument == 'e':
        with open('visits.txt', 'w') as file:
            for visit in visits:
                file.write('{0} {1}\n'.format(visit[0], visit[1]))
        print('Выход')
        break
    elif input_argument == 'd':
        with open('visits.txt') as file:
            for line in file:
                a = line.split()
                b = [None, None]
                b[0] = int(a[0])
                b[1] = int(a[1])
                visits.append(b)
    elif input_argument == 'v':
        curent_visit = input_visit()
        if curent_visit[0] and curent_visit[1]:
            visits.append(curent_visit)
        else:
            print('Визит не добавлен из-зи некорректно введенных данных.')
    elif input_argument == 'p':
        print(visits)
    elif input_argument == 'r':
        visits.remove(input_visit())
    elif input_argument == 'l':
        try:
            next_visit = int(input('Введите начало следующего визита: '))
        except ValueError:
            print('Некорректно введена дата.')
        try:
            if visits[-1][-1] <= next_visit <= SCHENGEN_CONSTRAINT:
                last_residence_limit = RESIDENCE_LIMIT - total_days_in_eu(visits)
                last_schengen_constraint = SCHENGEN_CONSTRAINT - next_visit
                if last_residence_limit > last_schengen_constraint:
                    print('Вы можете провести в EU {0} дней'.format(last_schengen_constraint))
                else:
                    print('Вы можете провести в EU {0} дней'.format(last_residence_limit))
            else:
                print('Дата визита должна быть больше {0} и меньше {}'.format(visits[-1][-1], SCHENGEN_CONSTRAINT))
        except IndexError:
            if SCHENGEN_CONSTRAINT - next_visit >= RESIDENCE_LIMIT:
                print('Вы можете провести в EU {0} дней'.format(RESIDENCE_LIMIT))
            else:
                print('Вы можете провести в EU {0} дней'.format(SCHENGEN_CONSTRAINT - next_visit))
    else:
        print('Неверно введенная команда, попробуйте еще раз.')
