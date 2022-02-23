N,M = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]
A.sort(reverse=True)
s = sum(A)
for a in A[:M]:
    if a < s/(4*M):
        print("No")
        break
else:
    print("Yes")