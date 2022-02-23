t = int(input())
for _ in range(t):
    s,n = [int(i) for i in input().split()]
    nums = [1]*n
    s -= n
    for i in range(10):