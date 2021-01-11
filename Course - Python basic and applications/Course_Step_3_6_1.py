# Текст задания: https://stepik.org/lesson/24474/step/4?unit=6779

# Вам дано описание пирамиды из кубиков в формате XML.
# Кубики могут быть трех цветов: красный (red), зеленый (green) и синий (blue).
# Для каждого кубика известны его цвет, и известны кубики, расположенные прямо под ним.
# # Пример:
# # <cube color="blue">
#   <cube color="red">
#     <cube color="green">
#     </cube>
#   </cube>
#   <cube color="red">
#   </cube>
# </cube>
#
# Введем понятие ценности для кубиков. Самый верхний кубик, соответствующий корню XML документа имеет ценность 1.
# Кубики, расположенные прямо под ним, имеют ценность 2. Кубики, расположенные прямо под нижележащими кубиками, имеют
# ценность 3. И т. д.
# # Ценность цвета равна сумме ценностей всех кубиков этого цвета.
# # Выведите через пробел три числа: ценности красного, зеленого и синего цветов.

from xml.etree import ElementTree

def count_weight(i, r):
    i += 1
    for child in r:
        d[child.attrib["color"]] += i
        count_weight(i, child)

root = ElementTree.fromstring(input())
d, i = {"red": 0, "green": 0, "blue": 0}, 1
d[root.attrib["color"]] = i
count_weight(i, root)

print(d["red"], d["green"], d["blue"])