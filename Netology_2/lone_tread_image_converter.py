# -*- coding: UTF-8 -*-

import subprocess
import os

if 'Result' not in os.listdir(os.getcwd()):
        os.mkdir('Result')

subprocess.run(['magick', 'Source\\*.jpg[200x113]', 'Result\\resize_wallpaper%03d.jpg'])
