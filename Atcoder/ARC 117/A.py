A,B = map(int, input().split())
E = [0]*(A+B)
if A > B:
    for i in range(1,A+1):
        E[i-1] = i
    sa = int((1+A)*(A) / 2)
    for i in range(1,B):
        E[A+i-1] = -i
        sa -= i
    E[-1] = -sa
else:
    for i in range(1,B+1):
        E[i-1] = -i
    sb = -int((1+B)*B / 2)
    for i in range(1,A):
        E[B+i-1] = i
        sb += i
    E[-1] = -sb
print(" ".join(map(str, E)))