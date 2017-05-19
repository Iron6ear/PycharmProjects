#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import subprocess
from multiprocessing import Pool
import os
import datetime


def result_dir_existing():
    if 'Result' not in os.listdir(os.getcwd()):
        os.mkdir('Result')


def list_of_image(path):
    list_of_images = os.listdir(path)
    return list_of_images


def resize_image(name):
    subprocess.run(['convert', os.path.join('Source', name), '-resize', '200', os.path.join('Result', 'RESIZED ' + name)])


def main():
    result_dir_existing()
    start = datetime.datetime.now()
    with Pool(4) as p:
        p.map(resize_image, list_of_image('Source'))
    end = datetime.datetime.now()
    print('Time for operations with files is {0:0.1f} second'.format((end-start).total_seconds()))

if __name__ == '__main__':
    main()
