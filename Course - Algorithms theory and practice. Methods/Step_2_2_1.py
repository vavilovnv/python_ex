# Текст задания: https://stepik.org/lesson/13228/step/6?unit=3414

# Дано целое число 1 ≤ n ≤ 40, необходимо вычислить n-е число Фибоначчи
# (напомним, что F_0 = 0, F_1 = 1, F_n = F_n-1 + F_n-2 при n ≥ 2).

def fib(n):
    a, b = 0, 1
    for _ in range(1, n):
        a, b = b, a + b
    return b


if __name__ == "__main__":
    n = int(input())
    print(fib(n))
