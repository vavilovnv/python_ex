# Текст задания: https://stepik.org/lesson/334150/step/4?auth=login&unit=317559

# Напишите функцию get_next_prime(num), которая принимает в качестве аргумента натуральное число num и возвращает первое
# простое число большее числа num.

def get_next_prime(num):
    while True:
        num += 1
        if len([i for i in range(1, num) if num % i == 0]) == 1:
            break
    return num


n = int(input())
print(get_next_prime(n))
