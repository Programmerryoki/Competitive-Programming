H, W = [int(i) for i in input().split()]
start = []
obj = []
goal = []
A = [[] for j in range(H)]
for a in range(len(A)):
    s = input()
    for b in range(len(s)):
        A[a].append(s[b])
        if s[b] == "R":
            start = [a,b]
        elif s[b] == "O":
            goal.append([a,b])

while len(goal) >= 1:
    pass