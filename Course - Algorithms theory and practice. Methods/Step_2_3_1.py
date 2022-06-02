# Текст задания: https://stepik.org/lesson/13229/step/5?unit=3415

# По данным двум числам 1 ≤ a,b ≤ 2 * 10^9 найдите их наибольший общий
# делитель.

def gcd(a, b):
    '''Реализация алгорима Евклида с применением рекурсии.'''
    if b == 0:
        return a
    return gcd(b, a % b)


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(gcd(a, b))
