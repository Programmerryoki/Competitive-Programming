value = [[11, 11], [4, 4], [3, 3], [20, 2], [10, 10], [14, 0], [0, 0], [0, 0]]
suit = "AKQJT987"

n, d = input().split()
total = 0
for a in range(int(n)):
    for b in range(4):
        v, s = list(input())
        total += value[suit.index(v)][0 if s == d else 1]
print(total)