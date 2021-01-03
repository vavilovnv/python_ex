# Текст задания: https://stepik.org/lesson/24466/step/9?unit=6773

import simplecrypt

with open('passwords.txt', 'r') as f:
    passwords = [i.strip() for i in f.readlines()]

with open('encrypted.bin', 'rb') as f:
    line = f.read()
    for passw in passwords:
        try:
            print(simplecrypt.decrypt(passw, line).decode('utf8'))
            break
        except simplecrypt.DecryptionException:
            pass

