#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import requests

YANDEX_API_KEY = 'trnsl.1.1.20170521T122626Z.0c79dbf1068d8641.5c5c6afea7197fe1c2af61bdf18a7589d588440c'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
LANG = 'ru-en'


def translate_me(text):
    parameters = {
        'key': YANDEX_API_KEY,
        'text': text,
        'lang': LANG
    }

    response = requests.get(URL, params=parameters)
    return response.json()


def main():
    json = translate_me('Привет, дорогой друг!')
    print(''.join(json['text']))

if __name__ == '__main__':
    main()
