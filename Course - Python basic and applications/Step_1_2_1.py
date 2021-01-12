# Текст задания: https://stepik.org/lesson/24458/step/9?unit=6765

# Реализуйте программу, которая будет вычислять количество различных объектов в списке.
# Два объекта a и b считаются различными, если a is b равно False.
#
# Вашей программе доступна переменная с названием objects, которая ссылается на список, содержащий не более 100
# объектов. Выведите количество различных объектов в этом списке.

objects = [int(i) for i in range(100)]

ans = len(objects)
for i in range(len(objects)-1):
    for j in range(i+1, len(objects)):
        if objects[i] is objects[j]:
            ans -= 1
            break
print(ans)
