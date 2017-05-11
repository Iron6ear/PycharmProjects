# -*- coding: UTF-8 -*-

import xml.etree.ElementTree as ET

tree = ET.parse('news_nnmclub.xml')
root = tree.getroot()
breakfast_menu_dict = dict()

for child in root:
    one_iter_dict = dict()
    for grandchild in child:
        if grandchild.tag != 'name':
            one_iter_dict[grandchild.tag] = grandchild.text
    breakfast_menu_dict[child[0].text] = one_iter_dict

print(breakfast_menu_dict)
