# Текст задания: https://stepik.org/lesson/245729/step/2?unit=217946

# Вася, открывший заправку в прошлом уроке, разорился. Конкуренция оказалась слишком большой. Вася предполагает, что это
# произошло от того, что теги заправки могут быть не только на точке, но и на каком-то контуре. Определите, сколько
# заправок на самом деле (не только обозначенных точкой) есть на фрагменте карты
# https://stepik.org/media/attachments/lesson/245681/map2.osm

import os, requests
import xml.etree.ElementTree as ET

osmfile = 'map2.osm'
res = requests.get('https://stepik.org/media/attachments/lesson/245681/' + osmfile)
if not os.access(osmfile, os.F_OK):
    with open(osmfile, 'wb') as f:
        f.write(res.content)
root = ET.parse(osmfile).getroot()
print(len(root.findall("./*/tag[@v='fuel']")))



