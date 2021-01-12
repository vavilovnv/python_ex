# Текст задания: https://stepik.org/lesson/24459/step/15?unit=6764

def c(n, k):
    if k > n:
        return 0
    if k == 0:
        return 1
    else:
        return c(n - 1, k) + c(n - 1, k - 1)

n, k = map(int, input().split())
print(c(n, k))