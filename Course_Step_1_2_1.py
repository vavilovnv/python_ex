# Реализуйте программу, которая будет вычислять количество различных объектов в списке.
# Два объекта a и b считаются различными, если a is b равно False.
# Вашей программе доступна переменная с названием objects, которая ссылается на список, содержащий не более 100 объектов. Выведите количество различных объектов в этом списке.
#
# Формат ожидаемой программы:
# ans = 0
# for obj in objects: # доступная переменная objects
#     ans += 1
# print(ans)

objects = [int(i) for i in range(100)]

ans = len(objects)
for i in range(len(objects)-1):
    for j in range(i+1, len(objects)):
        if objects[i] is objects[j]:
            ans -= 1
            break

print(ans)
