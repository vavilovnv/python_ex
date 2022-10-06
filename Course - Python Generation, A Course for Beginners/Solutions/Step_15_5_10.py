# Текст задания: https://stepik.org/lesson/352860/step/10?unit=336821

# На вход программе подается строка текста на английском языке, в которой нужно зашифровать все слова. Каждое слово
# строки следует зашифровать с помощью шифра Цезаря (циклического сдвига на длину этого слова). Строчные буквы при этом
# остаются строчными, а прописные – прописными.
#
# Формат входных данных
# На вход программе подается строка текста на английском языке.
#
# Формат выходных данных
# Программа должна вывести зашифрованный текст в соответствии с условием задачи.
#
# Примечание. Символы, не являющиеся английскими буквами, не изменяются.

def make_shift(c, dct, shift):
    delta = len(dct) if shift >= 0 else 0
    return dct[dct.find(c) + shift - delta]


def caesar_code(decode_word):
    new_s, len_word = '', 0
    for c in decode_word:
        if c.isalpha():
            len_word += 1
    for c in decode_word:
        if c in upper_en:
            new_s += make_shift(c, upper_en, len_word)
        elif c in lower_en:
            new_s += make_shift(c, lower_en, len_word)
        else:
            new_s += c
    return new_s


lower_en = 'abcdefghijklmnopqrstuvwxyz'
upper_en = lower_en.upper()
lst, new_lst = input().split(), []
for word in lst:
    new_lst.append(caesar_code(word))
print(*new_lst)
