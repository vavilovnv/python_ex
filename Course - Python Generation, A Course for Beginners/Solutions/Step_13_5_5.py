# Текст задания: https://stepik.org/lesson/334150/step/5?auth=login&unit=317559

# Напишите функцию is_password_good(password), которая принимает в качестве аргумента строковое значение пароля password
# и возвращает значение True если пароль является надежным и False в противном случае.
#
# Пароль является надежным если:
#
# его длина не менее 88 символов;
# он содержит как минимум одну заглавную букву (верхний регистр);
# он содержит как минимум одну строчную букву (нижний регистр);
# он содержит хотя бы одну цифру.

def is_password_good(password):
    return len(password) > 7 \
            and len([c for c in password if c.isupper()]) > 0 \
            and len([c for c in password if c.islower()]) > 0 \
            and len([c for c in password if c.isdigit()]) > 0


txt = input()
print(is_password_good(txt))

