def Bingo():
    for a in bingo:
        if sum(a) == 0:
            return True
    for b in range(len(bingo)):
        if sum([bingo[i][b] for i in range(3)]) == 0:
            return True
    if bingo[0][0] + bingo[1][1] + bingo[2][2] == 0:
        return True
    if bingo[1][1] + bingo[2][0] + bingo[0][2] == 0:
        return True
    return False

bingo = [[int(i) for i in input().split()] for i in range(3)]
valid = False
N = int(input())
for a in range(N):
    num = int(input())
    for b in range(len(bingo)):
        if num in bingo[b]:
            bingo[b][bingo[b].index(num)] = 0
    if Bingo():
        valid = True
        break
if valid:
    print("Yes")
else:
    print("No")