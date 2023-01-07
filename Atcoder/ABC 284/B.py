T = int(input())
for _ in range(T):
    N = int(input())
    print(sum(int(i)&1 for i in input().split()))