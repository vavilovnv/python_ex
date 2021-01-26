# Текст задания: https://stepik.org/lesson/21979/step/1?adaptive=true&unit=5238

# Требуется написать программу, осуществляющую преобразование из одних единиц измерения длины в другие.
# Должны поддерживаться
# мили (1 mile = 1609 m),
# ярды (1 yard = 0.9144 m),
# футы (1 foot = 30.48 cm),
# дюймы (1 inch = 2.54 cm),
# километры (1 km = 1000 m),
# метры (m),
# сантиметры (1 cm = 0.01 m)
# миллиметры (1 mm = 0.001 m)
# Используйте именно указанные в формулировке задачи единицы измерения с указанной точностью.
# Формат ввода:
# Одна строка с фразой следующего вида:
# <number> <unit_from> in <unit_to>
# например, если пришла фраза "15.5 mile in km", то требуется перевести 15.5 миль в километры.
# Формат вывода:
# Дробное число в научном формате (экспоненциальном), с точностью ровно два знака после запятой.

d = {'mile': 1609, 'yard': 0.9144, 'foot': 0.3048, 'inch': 0.0254, 'km': 1000, 'm': 1, 'cm': 0.01, 'mm': 0.001}
input = input().split()
print('{:3.2e}'.format(float(input[0]) * d[input[1]] / d[input[3]]))