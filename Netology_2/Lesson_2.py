# -*- coding: UTF-8 -*-
# Codding with russian: UTF-8, CP1251(windows-1251, CodePage-1251), KOI8-R, CP866, ISO8859-5
# Auto Decoder: https://www.artlebedev.ru/tools/decoder/
# https://docs.python.org/3/howto/unicode.html
# https://docs.python.org/3/library/codecs.html
# https://ru.wikipedia.org/wiki/Маркер_последовательности_байтов

import codecs

with codecs.open('newsit.json', encoding='cp1251') as news:
    print(news.read())

print(ord('э'))
print(chr(1101))

for x in range(ord('а'), ord('я') + 1):
    print(x, chr(x))
