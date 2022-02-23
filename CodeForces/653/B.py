t = int(input())
for _ in range(t):
    n = int(input())
    div = [0,0]
    while n%2 == 0:
        n //= 2
        div[0] += 1
    while n%3 == 0:
        n //= 3
        div[1] += 1
    if n != 1:
        print(-1)
        continue
    print((div[1] - div[0]) + (div[1]) if div[1] >= div[0] else -1)