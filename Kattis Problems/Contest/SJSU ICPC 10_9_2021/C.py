T = int(input())
for _ in range(T):
    n = int(input())
    ts = 0
    prev = 0
    for i in range(n):
        k,c = input().split(); k = int(k)
        k -= prev
        ts += 1
        prev = k
    print(ts)