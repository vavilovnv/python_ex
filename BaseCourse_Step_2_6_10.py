s, sp =  input(), []

while s != 'end':
    sp.append([int(i) for i in s.split()])
    s = input()

sp1 = list(sp)

for i in range(len(sp)):
    for j in range(len(sp[i])):
        sp1[i][j] = sp[i - 1][j] + sp[i - len(sp) + 1][j] + sp[i][j - 1] + sp[i][j - len(sp[i]) + 1]

print(sp1)
