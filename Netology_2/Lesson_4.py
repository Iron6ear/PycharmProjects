# -*- coding: UTF-8 -*-

# dir(какойто объект, что бы получить его свойства)
# help(краткая справка и документация)
# Windows: set USER_NAME=SomeName

import sys
import subprocess
import os

print(sys.argv)
print(os.environ['PATH'])
print('error', file=sys.stderr)
e = subprocess.run(['python', 'Lesson_2.py'])
print('Return code', e.returncode)
print('Program print: ', e.stdout)
print('===============')
