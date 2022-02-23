t = int(input())
for _ in range(t):
    n,m = map(int, input().split())
    print("YES" if sum([int(i) for i in input().split()]) == m else "NO")