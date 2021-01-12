# Текст задания: https://stepik.org/lesson/24460/step/10?unit=6766

def get(_ns, _v):
    if _ns == 'None':
        print(_ns)
    elif (_ns not in vs) or (_v not in vs[_ns]):
        for i in ns[_ns]:
            get(i, _v)
    elif _v in vs[_ns]:
        print(_ns)

def create(current, parent):
    if current in ns:
        ns[current] += [parent]
    else:
        ns[current] = [parent]

def add(names, var):
    if names in vs:
        vs[names] += [var]
    else:
        vs[names] = [var]

ns, vs = {'global': ['None']}, {'global': []}

for comm in [input().split() for i in range(int(input()))]:
    if comm[0] == 'create':
        create(comm[1], comm[2])
    elif comm[0] == 'add':
        add(comm[1], comm[2])
    else:
        get(comm[1], comm[2])


