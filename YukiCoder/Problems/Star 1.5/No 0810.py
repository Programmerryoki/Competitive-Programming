L,R,M = [int(i) for i in input().split()]
print(min(M, R - L + 1))