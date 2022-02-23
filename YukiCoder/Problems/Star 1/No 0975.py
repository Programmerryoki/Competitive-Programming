X,N,M = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]
if X in A and X in B:
    print("MrMaxValu")
elif X in A:
    print("MrMax")
elif X in B:
    print("MaxValu")
else:
    print(-1)