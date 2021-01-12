# Текст задания: https://stepik.org/lesson/3380/step/1?unit=963

def add_team(k1, k2):

    if k1[0] not in teams:
        teams[k1[0]] = [0, 0, 0, 0, 0]

    teams[k1[0]][0] += 1
    if k1[1] > k2[1]:
        teams[k1[0]][1] += 1
        teams[k1[0]][4] += 3
    elif k1[1] == k2[1]:
        teams[k1[0]][2] += 1
        teams[k1[0]][4] += 1
    else:
        teams[k1[0]][3] += 1

teams = {}
for i in range(int(input())):
    game = input().split(';')
    add_team([game[0], int(game[1])], [game[2], int(game[3])])
    add_team([game[2], int(game[3])], [game[0], int(game[1])])

for team, scores in teams.items():
    print(team, end=':')
    print(*scores)
