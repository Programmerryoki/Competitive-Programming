X = input()
N = int(input())
ind = {X[i]:i for i in range(26)}
S = [input() for i in range(N)]
S.sort(key=lambda x: list(ind[i] for i in x))
print("\n".join(S))