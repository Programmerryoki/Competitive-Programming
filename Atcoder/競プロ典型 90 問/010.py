from itertools import accumulate

N = int(input())
class1 = [0]*N
class2 = [0]*N
for i in range(N):
    C,P = map(int, input().split())
    if C == 1:
        class1[i] = P
    else:
        class2[i] = P
ac1 = [0]+list(accumulate(class1))
ac2 = [0]+list(accumulate(class2))
# print(ac1, ac2)
Q = int(input())
ans = [""]*Q
for i in range(Q):
    L,R = map(int, input().split())
    a1 = ac1[R] - ac1[L-1]
    a2 = ac2[R] - ac2[L-1]
    ans[i] += str(a1)+" "+str(a2)
print("\n".join(ans))