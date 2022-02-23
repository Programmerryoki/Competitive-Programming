from itertools import permutations

S,K = input().split(); K = int(K)
pos = set()
for p in permutations(S, len(S)):
    pos.add("".join(p))
pos = sorted(pos)
print(pos[K-1])