N = int(input())
A = [int(i) for i in input().split()]
su = 0
for i in range(N):
    for j in range(i+1,N+1):
        print("\t"*i + " ".join(map(str, A[i:j])))
        su += sum(A[i:j])
s = 0
for i,n in enumerate(A):
    s += n*(N - i)*(i + 1)
# print(s, su)
print(s)