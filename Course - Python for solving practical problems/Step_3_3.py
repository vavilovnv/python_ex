# Текст задания: https://stepik.org/lesson/245681/step/2?unit=217898

# Вася решил открыть АЗС (заправку). Чтобы оценить уровень конкуренции он хочет изучить количество заправок в
# интересующем его районе. Вася скачал интересующий его кусок карты OSM
# https://stepik.org/media/attachments/lesson/245681/map2.osm и хочет посчитать, сколько на нём отмечено точечных
# объектов (node), являющихся заправкой. В качестве ответа вам необходимо вывести одно число - количество АЗС.
# "Как обозначается заправка в OpenStreetMap" - пример хорошего запроса чтобы узнать, как обозначается заправка в
# OpenStreetMap.

import os, wget
import xml.etree.ElementTree as ET

osmfile = 'map2.osm'
if not os.access(osmfile, os.F_OK):
    wget.download('https://stepik.org/media/attachments/lesson/245681/' + osmfile)
print(len(ET.parse(osmfile).getroot().findall("./node/tag[@v='fuel']")))



