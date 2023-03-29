"""
Write a function that builds a tree based on a list of tuples of id (parent id, offspring id),
where None is the id of the root node.
How this should work:
Написать функцию, строящую дерево по списку пар id (id родителя, id потомка),
где None - id корневого узла.
Пример работы:
"""

source = [
    (None, 'a'),
    (None, 'b'),
    (None, 'c'),
    ('a', 'a1'),
    ('a', 'a2'),
    ('a2', 'a21'),
    ('a2', 'a22'),
    ('b', 'b1'),
    ('b1', 'b11'),
    ('b11', 'b111'),
    ('b', 'b2'),
    ('c', 'c1'),
]

expected = {
    'a': {'a1': {}, 'a2': {'a21': {}, 'a22': {}}},
    'b': {'b1': {'b11': {'b111': {}}}, 'b2': {}},
    'c': {'c1': {}},
}


# рекурсивное решение, которое не приняли (хотя никаких ограничений не было)
def to_tree(source):
    def helper(key, d):
        for pair in source:
            if pair[0] == key:
                d[pair[1]] = {}
                helper(pair[1], d[pair[1]])
    res = {}
    helper(None, res)
    return res


assert to_tree(source) == expected


# линейное решение, написал потом, когда узнал, что рекурсия нежелательна
def to_tree(source):
    res = {v: {} for k, v in source if k is None}
    for item in source:
        if item[0] is None:
            continue
        tmp = res
        for count in range(len(item[0]) - 1, -1, -1):
            if item[0] in tmp:
                tmp[item[0]].update({item[1]: {}})
                break
            tmp = tmp[item[0][:-count]]
    return res


assert to_tree(source) == expected
