n,d = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]
used = set()
pos = []
for i in range(n):
    if A[i] == -1:
        pos.append(i)
    else:
        used.add(A[i])
rem = set(i+1 for i in range(n)) - used
print(rem)