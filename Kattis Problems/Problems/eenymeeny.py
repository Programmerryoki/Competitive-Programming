rhyme = input().split()
n = int(input())
kids = []
team1 = []
team2 = []
for a in range(n):
    kids.append(input())

turn = 0
ki = 0
index = 0
while len(kids) > 0:
    index = (len(rhyme) + ki - 1 + index) % len(kids)
    if turn == 0:
        team1.append(kids.pop(index))
        turn = 1
    elif turn == 1:
        team2.append(kids.pop(index))
        turn = 0
print(len(team1))
for a in team1:
    print(a)
print(len(team2))
for a in team2:
    print(a)