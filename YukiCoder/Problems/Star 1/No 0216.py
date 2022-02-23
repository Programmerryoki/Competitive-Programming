N = int(input())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]
solved = [0]*100
pp = 0
for i,a in enumerate(A):
    if B[i] == 0:
        pp += a
    else:
        solved[B[i]-1] += a
print("YES" if pp >= max(solved) else "NO")