# Текст задания: https://stepik.org/lesson/334150/step/8?auth=login&unit=317559

# BEEGEEK наконец открыл свой банк в котором используются специальные банкоматы с необычным паролем.
#
# Действительный пароль BEEGEEK банка имеет вид a:b:c, где a, b и c – натуральные числа. Поскольку основатель BEEGEEK
# фанатеет от математики, то он решил:
#
# число a – должно быть палиндромом;
# число b – должно быть простым;
# число c – должно быть четным.
# Напишите функцию is_valid_password(password), которая принимает в качестве аргумента строковое значение пароля
# password и возвращает значение True если пароль является действительным паролем BEEGEEK банка и False в противном
# случае.

def is_valid_password(password):
    lst = password.split(':')
    return len(lst) == 3 and lst[0][::] == lst[0][::-1] \
            and len([i for i in range(1, int(lst[1])) if int(lst[1]) % i == 0]) == 1 \
            and int(lst[2]) % 2 == 0


print(is_valid_password(input()))