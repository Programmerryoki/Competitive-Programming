t = int(input())
for _ in range(t):
    l,r = [int(i) for i in input().split()]
    print(r % max(r//2+1, l))