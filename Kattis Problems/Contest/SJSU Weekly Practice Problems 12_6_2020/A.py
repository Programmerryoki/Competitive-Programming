hands = "RPS"

R = int(input())
sven = [hands.index(i) for i in input()]
N = int(input())
friends = [[hands.index(i) for i in input()] for j in range(N)]
# print(sven, friends)
ascore = 0
for i in range(N):
    # print([2 if sven[j] - friends[i][j] in [1,-2] else 1 if sven[j] == friends[i][j] else 0 for j in range(R)])
    ascore += sum([2 if sven[j] - friends[i][j] in [1,-2] else 1 if sven[j] == friends[i][j] else 0 for j in range(R)])
print(ascore)
ms = 0
for i in range(R):
    temp = 0
    for k in range(3):
        temp = max(temp, sum([2 if k - friends[j][i] in [1,-2] else 1 if k == friends[j][i] else 0 for j in range(N)]))
    ms += temp
print(ms)