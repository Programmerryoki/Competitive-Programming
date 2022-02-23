from itertools import permutations

N,M = [int(i) for i in input().split()]
g1 = {i:set() for i in range(N)}
for _ in range(M):
    A,B = [int(i)-1 for i in input().split()]
    g1[A].add(B)
    g1[B].add(A)
g2 = {i:set() for i in range(N)}
for _ in range(M):
    C,D = [int(i)-1 for i in input().split()]
    g2[C].add(D)
    g2[D].add(C)
for order in permutations([i for i in range(N)],N):
    bij = {i:order[i] for i in range(N)}
    for key in g1:
        for val in g1[key]:
            if bij[val] not in g2[bij[key]]:
                break
        else:
            continue
        break
    else:
        print("Yes")
        exit()
print("No")