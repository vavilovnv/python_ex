# Условие задачи https://stepik.org/lesson/13239/step/5?unit=3425

# По данной непустой строке s длины не более 10^4, состоящей из строчных букв
# латинского алфавита, постройте оптимальный беспрефиксный код. В первой
# строке выведите количество различных букв k, встречающихся в строке, и
# # размер получившейся закодированной строки. В следующих k строках запишите
# коды букв в формате "letter: code". В последней строке выведите
# закодированную строку.

def huffman_encrypt(string_to_encrypt: str) -> dict:
    """Функция формирует таблицу Хаффмана в виде словаря "буква - код из нулей
    и едениц" для переданной строки текста. Принцип алгоритма базируется на
    формировании бинарного кода для каждого символа из дерева с частотой
    встреч каждого из символов строки. При этом само дерево не строится, его
    заменяет список freq, каждый элемент которого представляет собой сумму
    подстрок с наименьшим весом-частотой."""
    
    various, d, freq = set(list(string_to_encrypt)), {}, []
    lst = sorted(([c, s.count(c)] for c in various), key=lambda x: x[1])
    if len(lst) == 1:
        freq.append([lst.pop(0)[0], 0])
    else:
        while len(lst) > 1:
            f1, f2 = lst.pop(0), lst.pop(0)
            lst.append([f1[0] + f2[0], f1[1] + f2[1]])
            freq.append([f1[0], 0])
            freq.append([f2[0], 1])
            lst = sorted(lst, key=lambda x: x[1])
    for c in various:
        for f in freq[::-1]:
            if c in f[0]:
                if c not in d:
                    d[c] = d.get(c, str(f[1]))
                else:
                    d[c] += str(f[1])
    return d


if __name__ == '__main__':
    s = input()
    huffman_table = huffman_encrypt(s)
    code = ''.join([huffman_table[c] for c in s])
    print(len(huffman_table), len(code))
    [print(f'{c}: {huffman_table[c]}') for c in sorted(huffman_table)]
    print(code)
