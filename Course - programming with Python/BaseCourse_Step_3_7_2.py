# Текст задания https://stepik.org/lesson/3380/step/2?unit=963

def code_decode(d, w):
    for i in range(len(w)):
        if w[i] in d:
            print(d[w[i]], end='')
    print()

l1, l2, w1, w2 = (input() for i in range(4))
code_decode({l1[i]: l2[i] for i in range(len(l1))}, w1)
code_decode({l2[i]: l1[i] for i in range(len(l2))}, w2)


