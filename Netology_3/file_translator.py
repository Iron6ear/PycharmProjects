#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import requests

YANDEX_API_KEY = 'trnsl.1.1.20170521T122626Z.0c79dbf1068d8641.5c5c6afea7197fe1c2af61bdf18a7589d588440c'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
LANG = ['ru-en', 'de-ru', 'fr-ru', 'it-ru']


def translate_me(text, lang):
    """
    Синтаксис запроса

    https://translate.yandex.net/api/v1.5/tr.json/translate ? 
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]
    key	
    API-ключ. Выдается бесплатно.
    text	
    Текст, который необходимо перевести.
    В запросе можно использовать несколько параметров text.
    Внимание! 
    Для исходного текста обязательно используйте URL-кодировние.
    Ограничения:
    Для POST-запросов максимальный размер передаваемого текста составляет 10 000 символов.
    В GET-запросах ограничивается не размер передаваемого текста, а размер всей строки запроса,
    которая кроме текста может содержать и другие параметры.
    Максимальный размер строки — от 2 до 10 КБ (зависит от версии используемого браузера).
    lang	
    Направление перевода.
    Может задаваться одним из следующих способов:
    В виде пары кодов языков («с какого»-«на какой»), разделенных дефисом.
    Например, en-ru обозначает перевод с английского на русский.
    В виде кода конечного языка (например ru). В этом случае сервис пытается определить исходный язык автоматически.
    format	
    Формат текста.
    Возможные значения:
    plain — текст без разметки (значение по умолчанию);
    html — текст в формате HTML.
    options	
    В настоящее время доступна единственная опция — признак включения в ответ автоматически определенного
    языка переводимого текста.
    Этому соответствует значение 1 этого параметра.
    Если язык переводимого текста задан в явном виде, т. е. параметр lang представлен в виде пары кодов,
    то первый код однозначно определяет исходный язык.
    Это означает, что параметр options не позволяет переключиться в режим автоматического определения языка.
    Однако он позволяет понять, правильно ли был указан исходный язык в параметре lang.
    callback	Имя функции обратного вызова. Используется для получения JSONP-ответа.
    Примечание. Все специальные символы должны быть экранированы.
    :param text: 
    :return: 
    """
    parameters = {
        'key': YANDEX_API_KEY,
        'text': text,
        'lang': lang
    }

    response = requests.get(URL, params=parameters)
    return response.json()


def get_text(path):
    with open(path) as FD:
        return FD.read()


def main():
    text = get_text('ITL.txt')
    json = translate_me(text, LANG[3])
    print(''.join(json['text']))


if __name__ == '__main__':
    main()
