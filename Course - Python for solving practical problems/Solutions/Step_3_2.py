# Текст задания: https://stepik.org/lesson/245678/step/2?unit=217895

# В OpenStreetMap XML встречаются теги node, которые соответствуют некоторым точкам на карте. Ноды могут не только
# обозначать какой-то точечный объект, но и входить в состав way (некоторой линии, возможно замкнутой) и не иметь
# собственных тегов. Для доступного по ссылке https://stepik.org/media/attachments/lesson/245678/map1.osm фрагмента
# карты посчитайте, сколько node имеет хотя бы один вложенный тэг tag, а сколько - не имеют. В качестве ответа введите
# два числа, разделённых пробелом.

import os, wget
import xml.etree.ElementTree as ET

osmfile = 'map1.osm'
if not os.access(osmfile, os.F_OK):
    wget.download('https://stepik.org/media/attachments/lesson/245678/' + osmfile)
root = ET.parse(osmfile).getroot()
nodes = [False if child.find('tag') == None else True for child in root.findall('node')]
print(nodes.count(True), nodes.count(False))




