# Условие задачи https://stepik.org/lesson/13238/step/11?unit=3424

# По данному числу 1≤n≤10^9 найдите максимальное число k, для которого n можно представить как сумму k различных
# натуральных слагаемых. Выведите в первой строке число k, во второй — k слагаемых.

n = int(input())
summations, i = [], 1
while n - i > i:
    summations.append(i)
    n -= i
    i += 1
summations.append(n)
print(len(summations))
print(*summations)




