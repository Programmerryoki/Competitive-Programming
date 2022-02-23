n = int(input())
teams = []
uni = []
for a in range(n):
    team = input().split()
    if team[0] not in uni:
        uni.append(team[0])
        teams.append(team[1])

for a in range(12):
    print(uni[a], teams[a])