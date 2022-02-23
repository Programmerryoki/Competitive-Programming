noChess = [1, 1, 2, 2, 2, 8]
actual = [int(i) for i in input().split()]
for a in range(len(noChess)):
    noChess[a] = noChess[a] - actual[a]
print(" ".join(map(str,noChess)))