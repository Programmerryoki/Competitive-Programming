t = int(input())
for _ in range(t):
    n,s = [int(i) for i in input().split()]
    print(s // -(-(n+1)//2))