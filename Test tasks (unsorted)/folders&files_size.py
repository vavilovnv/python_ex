# определение размера папок и файлов в текущей директории (например для удаления)
from os import listdir, path, walk


def get_folder_size(start_path='.'):
    total_size = 0

    for dirpath, dirnames, filenames in walk(start_path):
        total_size += sum(path.getsize(path.join(dirpath, name)) for name in filenames)

    return total_size


def format_size(size):
    size_format = {1: 'Б', 2: 'КБ', 3: 'МБ', 4: 'ГБ'}

    count = 1
    while size >= 1024:
        count += 1
        size /= 1024

    return f'{round(size)} {size_format[count]}'


def to_remove(top_size=10):
    folders = list(filter(path.isdir, listdir()))
    files = list(filter(path.isfile, listdir()))

    content = []

    content += list(map(lambda name: (get_folder_size(name), name), folders)) if folders else []
    content += list(map(lambda name: (path.getsize(name), name), files)) if files else []

    content.sort(key=lambda x: x[0], reverse=True)
    content = map(lambda size_name: f'{format_size(size_name[0])} {size_name[1]}', content[:top_size])

    return '\n'.join(content)


print(to_remove())