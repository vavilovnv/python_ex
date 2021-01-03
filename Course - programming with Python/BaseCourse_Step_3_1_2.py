# Текст задания: https://stepik.org/lesson/3372/step/9?unit=955

lst = [10, 5, 8, 3]

def modify_list(lst):

    for i in range(len(lst)-1,-1,-1):
        if lst[i]%2 == 0:
            lst[i] = int(lst[i]/2)
        else:
            lst.remove(lst[i])

modify_list(lst)
print(*lst)