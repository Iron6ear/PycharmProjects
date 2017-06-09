#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Реализуйте класс доступа к API Яндекс.Метрика, который принимает токен и предоставляет информацию о визитах,
# просмотрах и посетителях.
# Зачёт с отличием: разбейте класс на базовый, который будет определять общую логику работы и подклассы, в которых будет
# функционал для работы с конкретным набором вызовов(допустим Базовый класс, Подкласс для работы с API отчётов и
# Подкласс для работы с API управления).

# https://yandex.ru/support/metrika/
# https://tech.yandex.ru/metrika/
# https://tech.yandex.ru/metrika/doc/api2/concept/about-docpage/
# https://tech.yandex.ru/oauth/doc/dg/concepts/ya-oauth-intro-docpage/
# https://ru.wikipedia.org/wiki/OAuth
# https://jekyllrb.com/
# https://www.python.org/download/releases/2.3/mro/
# https://habrahabr.ru/post/62203/

TOKEN = '66be9c9a14fb43a78014660a81e241e6'

class A():
    def __init__(self, TOKEN):
        self.token = TOKEN