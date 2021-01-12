# Условие задачи: https://stepik.org/lesson/24463/step/7?auth=login&unit=6771

def is_ancestor(ans, exc):
    if ans in except_h[exc]:
        return True
    else:
        check = False
        for i in except_h[exc]:
            if i != exc:
                check = is_ancestor(ans, i)
                if check:
                    return True
        return False

except_h = {}
for line in [input().strip().split() for i in range(int(input()))]:
    except_h[line[0]] = [line[0]]
    if len(line) > 1:
        except_h[line[0]] += line[2:]

exceptions = [input() for i in range(int(input()))]

for i in range(1, len(exceptions)):
    for j in range(i):
        if is_ancestor(exceptions[j], exceptions[i]):
            print(exceptions[i])
            break