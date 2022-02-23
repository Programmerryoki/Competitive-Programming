N = int(input())


def calc(x):
    if x == 1:
        return 1
    return ((x + 1) * x) // 2


for n in range(int(N**0.5), N+1):
    if calc(n) < N:
        continue
    print(n)
    break