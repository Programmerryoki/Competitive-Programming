N = int(input())
for _ in range(N):
    K, *O = [int(i) for i in input().split()]
    print(sum(O)-K+1)